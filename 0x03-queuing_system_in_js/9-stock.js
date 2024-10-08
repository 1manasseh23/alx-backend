import express from 'express';
import redis from 'redis';
import { promisify } from 'util';

const app = express();
const port = 1245;

const listProducts = [
    { id: 1, name: 'Suitcase 250', price: 50, stock: 4 },
    { id: 2, name: 'Suitcase 450', price: 100, stock: 10 },
    { id: 3, name: 'Suitcase 650', price: 350, stock: 2 },
    { id: 4, name: 'Suitcase 1050', price: 550, stock: 5 } 
];

// Create Redis client
const client = redis.createClient();

// Promisify Redis methods
const getAsync = promisify(client.get).bind(client);
const setAsync = promisify(client.set).bind(client);

async function reserveStockById(itemId, stock) {
    await setAsync(`item.${itemId}`, stock);
}

async function getCurrentReservedStockById(itemId) {
    const stock = await getAsync(`item.${itemId}`);
    return stock ? parseInt(stock) : null;
}


function getItemById(id) {
    return listProducts.find(item => item.id === id);
}

app.get('/list_products', (req, res) => {
    const products = listProducts.map(product => ({
        itemId: product.id,
        itemName: product.name,
        price: product.price,
        initialAvailableQuantity: product.stock
    }));
    res.json(products);
});

app.get('/list_products/:itemId', async (req, res) => {
    const itemId = parseInt(req.params.itemId);
    const product = getItemById(itemId);

    if (!product) {
        return res.json({ status: 'Product not found' });
    }

    const currentStock = await getCurrentReservedStockById(itemId);
    const currentQuantity = currentStock !== null ? currentStock : product.stock;

    res.json({
        itemId: product.id,
        itemName: product.name,
        price: product.price,
        initialAvailableQuantity: product.stock,
        currentQuantity: currentQuantity
    });
});

app.get('/reserve_product/:itemId', async (req, res) => {
    const itemId = parseInt(req.params.itemId);
    const product = getItemById(itemId);

    if (!product) {
        return res.json({ status: 'Product not found' });
    }

    const currentStock = await getCurrentReservedStockById(itemId);
    const availableStock = currentStock !== null ? currentStock : product.stock;

    if (availableStock <= 0) {
        return res.json({
            status: 'Not enough stock available',
            itemId: product.id
        });
    }

    await reserveStockById(itemId, availableStock - 1);

    res.json({
        status: 'Reservation confirmed',
        itemId: product.id
    });
});

app.listen(port, () => {
    console.log(`Server listening on port ${port}`);
});

