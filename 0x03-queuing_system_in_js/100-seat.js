import redis from 'redis';
import { promisify } from 'util';
import kue from 'kue';
import express from 'express';

const app = express();
const port = 1245;

const queue = kue.createQueue();

// Create Redis client
const client = redis.createClient();

// Promisify Redis methods
const getAsync = promisify(client.get).bind(client);
const setAsync = promisify(client.set).bind(client);

// Function to reserve seats
async function reserveSeat(number) {
    await setAsync('available_seats', number);
}

// Function to get current available seats
async function getCurrentAvailableSeats() {
    const seats = await getAsync('available_seats');
    return parseInt(seats, 10);
}

// Function to initialize seats and reservation status
async function initializeSeats() {
    await reserveSeat(50);
    reservationEnabled = true;
}

let reservationEnabled = true;

// Initialize the seats
initializeSeats().catch(console.error);

// Route to get the current number of available seats
app.get('/available_seats', async (req, res) => {
    const availableSeats = await getCurrentAvailableSeats();
    res.json({ numberOfAvailableSeats: availableSeats });
});

// Route to reserve a seat
app.get('/reserve_seat', (req, res) => {
    if (!reservationEnabled) {
        return res.json({ status: 'Reservation are blocked' });
    }

    const job = queue.create('reserve_seat').save((err) => {
        if (err) {
            return res.json({ status: 'Reservation failed' });
        }
        res.json({ status: 'Reservation in process' });
    });

    job.on('complete', () => {
        console.log(`Seat reservation job ${job.id} completed`);
    }).on('failed', (errorMessage) => {
        console.log(`Seat reservation job ${job.id} failed: ${errorMessage}`);
    });
});

// Route to process the reservation queue
app.get('/process', (req, res) => {
    res.json({ status: 'Queue processing' });

    queue.process('reserve_seat', async (job, done) => {
        const availableSeats = await getCurrentAvailableSeats();

        if (availableSeats <= 0) {
            reservationEnabled = false;
            return done(new Error('Not enough seats available'));
        }

        const newSeats = availableSeats - 1;
        await reserveSeat(newSeats);

        if (newSeats === 0) {
            reservationEnabled = false;
        }

        done();
    });
});

app.listen(port, () => {
    console.log(`Server listening on port ${port}`);
});

