const WebSocket = require('ws');

const server = new WebSocket.Server({ port: 8080 });



server.on('connection', (socket) => {
  console.log('Client connected');

  // Send a welcome message to the connected client
  socket.send('Welcome to the WebSocket server!');

  // Listen for messages from the client
  socket.on('message', (message) => {
    console.log(`Received message: ${message}`);
    socket.send(`Server has receaved the message:  ${message}`);
  });

  // Handle client disconnection
  socket.on('close', () => {
    console.log('Client disconnected');
  });

  // Handle errors
  socket.on('error', (error) => {
    console.error(`WebSocket error: ${error}`);
  });
});

console.log('WebSocket server running on port 8080');
