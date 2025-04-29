import express from 'express';
import bodyParser from 'body-parser';
import cors from 'cors';
import studentRoutes from './routes/studentRoutes';

const app = express();
const PORT = 4000;

app.use(cors());
app.use(bodyParser.json());

// Route registration
app.use('/api/students', studentRoutes);

app.get('/', (_, res) => {
  res.send('Welcome to NOVA API - Backend is running.');
});

app.listen(PORT, () => {
  console.log(`✅ Server running on http://localhost:${PORT}`);
});
