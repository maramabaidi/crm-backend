const express = require('express');
const bodyParser = require('body-parser');
const dotenv = require('dotenv');
const cors = require('cors');
const productRoutes = require('./routes/productRoutes');
const connectDB = require('./config/db'); // Fix the import

dotenv.config();

const app = express();

// Middleware
app.use(cors());
app.use(bodyParser.json());
app.use('/api/products', productRoutes);

// Connect to MongoDB
connectDB(); // Call the connectDB function

// Start Server
const PORT = process.env.PORT || 5000;
app.listen(PORT, () => {
    console.log(`Product Service running on port ${PORT}`);
});
