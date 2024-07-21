
import kue from 'kue';

const queue = kue.createQueue();

const data = {
    phoneNumber: '061234567',
    message: 'Im a test sentence',
};

const job = queue.create('push_notification_code', data).save((err) => {
    if (!err) {
        console.log(`Notification job created: ${job.id}`);
    } else {
        console.error('Could not create job:', err);
    }
});

job.on('complete', () => {
    console.log('Notification job completed')
});

job.on('failed', () => {
    console.log('Notification job failed')
});
