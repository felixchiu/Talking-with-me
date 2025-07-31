# Talking-with-me

A modern, real-time chat application built with Flask, SocketIO, and Bulma CSS framework.

## Features

- 🎨 **Modern UI**: Beautiful interface using Bulma CSS framework
- 💬 **Real-time Messaging**: Instant message delivery using WebSocket
- 👥 **User Tracking**: Live user count display
- 📱 **Responsive Design**: Works perfectly on desktop and mobile
- 🔗 **Connection Status**: Visual connection status indicator
- ⚡ **Fast & Lightweight**: No JavaScript framework required

## Screenshots

The app features a modern chat interface with:
- Hero section with gradient background
- Chat bubbles with different styles for sent/received messages
- Real-time connection status
- User count display
- Responsive design that works on all devices

## Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd Talking-with-me
   ```

2. **Create virtual environment**
   ```bash
   python -m venv flask_socketio_venv
   source flask_socketio_venv/bin/activate  # On Windows: flask_socketio_venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   python app.py
   ```

5. **Open your browser**
   Navigate to `http://localhost:5000`

## Usage

1. **Start the server**: Run `python app.py`
2. **Open multiple browser tabs**: Visit `http://localhost:5000` in different tabs
3. **Start chatting**: Type messages and see them appear in real-time across all tabs
4. **Monitor connections**: Watch the connection status and user count update automatically

## Technology Stack

- **Backend**: Flask + Flask-SocketIO
- **Frontend**: HTML5 + JavaScript + Socket.IO Client
- **Styling**: Bulma CSS Framework
- **Icons**: Font Awesome
- **Real-time Communication**: WebSocket via Socket.IO

## Key Features Explained

### Modern UI with Bulma
- Uses Bulma CSS framework for clean, modern styling
- Responsive grid system that adapts to screen size
- Beautiful gradient backgrounds and smooth animations
- Professional typography and spacing

### Real-time Communication
- WebSocket connection for instant message delivery
- Connection status monitoring with visual indicators
- Automatic reconnection handling
- User count tracking in real-time

### Enhanced UX
- Message bubbles with different styles for sent/received messages
- Smooth fade-in animations for new messages
- Auto-scroll to latest messages
- Enter key support for sending messages
- Focus management for better accessibility

## Project Structure

```
Talking-with-me/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── templates/
│   └── index.html        # Main chat interface
└── README.md            # This file
```

## Customization

### Styling
The app uses Bulma CSS classes and custom CSS. You can customize:
- Colors in the CSS variables
- Message bubble styles
- Hero section gradients
- Button and input styling

### Features
You can extend the app with:
- User authentication
- Private messaging
- File sharing
- Message persistence
- Typing indicators
- Read receipts

## Browser Support

- Chrome 60+
- Firefox 55+
- Safari 12+
- Edge 79+

## Development

To run in development mode:
```bash
python app.py
```

The app will be available at `http://localhost:5000` with hot-reload enabled.

## Production Deployment

For production deployment, consider:
- Using a production WSGI server (Gunicorn)
- Setting up proper SSL certificates
- Implementing user authentication
- Adding message persistence with a database
- Using environment variables for configuration

## License

This project is open source and available under the MIT License.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

---

Built with ❤️ using Flask, SocketIO, and Bulma CSS

## About

Talking-with-me is a modern, responsive chat application that demonstrates real-time communication using WebSocket technology. Perfect for learning about real-time web applications or as a foundation for more complex chat systems. 