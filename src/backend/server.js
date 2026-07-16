const express = require('express');
const bodyParser = require('body-parser');

const app = express();
app.use(bodyParser.json());

// Dummy data for demonstration purposes
let users = [
    { id: 1, name: 'John Doe', email: 'john@example.com' },
    { id: 2, name: 'Jane Smith', email: 'jane@example.com' }
];

// API route to get all users
app.get('/api/users', (req, res) => {
    res.json(users);
});

// API route to create a new user
app.post('/api/users', (req, res) => {
    const newUser = {
        id: Date.now(),
        name: req.body.name,
        email: req.body.email
    };
    users.push(newUser);
    res.status(201).json(newUser);
});

// API route to get a single user by ID
app.get('/api/users/:id', (req, res) => {
    const userId = parseInt(req.params.id);
    const user = users.find(u => u.id === userId);
    if (user) {
        res.json(user);
    } else {
        res.status(404).json({ message: 'User not found' });
    }
});

// API route to update a user by ID
app.put('/api/users/:id', (req, res) => {
    const userId = parseInt(req.params.id);
    const updatedUser = users.find(u => u.id === userId);
    if (updatedUser) {
        updatedUser.name = req.body.name;
        updatedUser.email = req.body.email;
        res.json(updatedUser);
    } else {
        res.status(404).json({ message: 'User not found' });
    }
});

// API route to delete a user by ID
app.delete('/api/users/:id', (req, res) => {
    const userId = parseInt(req.params.id);
    users = users.filter(u => u.id !== userId);
    res.status(204).send();
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});