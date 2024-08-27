import kue from 'kue';

function createPushNotificationsJobs(jobs, queue) {
  // Check if jobs is an array
  if (!Array.isArray(jobs)) {
    throw new Error('Jobs is not an array');
  }

  // Iterate over each job in the jobs array
  jobs.forEach((jobData) => {
    // Create a new job in the queue 'push_notification_code_3'
    const job = queue.create('push_notification_code_3', jobData);

    // Event: When job is created successfully
    job.on('enqueue', () => {
      console.log(`Notification job created: ${job.id}`);
    });

    // Event: When job completes
    job.on('complete', () => {
      console.log(`Notification job ${job.id} completed`);
    });

    // Event: When job fails
    job.on('failed', (error) => {
      console.log(`Notification job ${job.id} failed: ${error}`);
    });

    // Event: Track job progress
    job.on('progress', (progress) => {
      console.log(`Notification job ${job.id} ${progress}% complete`);
    });

    // Save the job to the queue
    job.save();
  });
}

export default createPushNotificationsJobs;

