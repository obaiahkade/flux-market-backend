# flux-market-backend

The core backend service for Flux Market, designed to handle real-time data streaming, e-commerce transactions, and seamless client-server communication using a Django and ASGI architecture.

## 🚀 What Problem It Solves

Traditional market platforms often struggle with real-time data delivery. **Flux Market** solves this by utilizing persistent WebSocket connections to stream high-frequency data (such as market fluctuations or system logs) instantly to the client. This ensures that users see data updates in real-time with minimal latency, creating a highly responsive and dynamic user experience.

## 🏗️ Project Architecture

The architecture is built for asynchronous processing and real-time communication:

*   **Backend Framework:** Built with **Django**, containing dedicated apps for `core_marketplace` and `ecommerce_platform`.
*   **ASGI Server:** Runs on **Daphne**, allowing the application to handle traditional HTTP requests and long-lived WebSocket connections concurrently.
*   **Database:** Uses SQLite (`db.sqlite3`) for local development and structured data storage, alongside custom SQL schemas (`logs_schema.sql`).
*   **Data Generation:** The `send_mock_logs.py` script acts as an internal data producer, simulating live market events or system logs.

## ⚙️ How It Works

1.  **Initialization:** The backend application is booted up via `run_daphne.py`, opening up both standard Django HTTP routes and WebSocket routing.
2.  **Data Ingestion:** The `send_mock_logs.py` script is executed, continuously generating mock data and pushing it into the backend system.
3.  **Real-Time Broadcasting:** As the backend receives new data, it immediately pushes these updates through open WebSocket channels to any connected clients.

## 🖥️ UI Integration

The frontend UI is designed to seamlessly integrate with this backend. 
*   **API Endpoints:** The UI fetches initial historical data, product listings, or configuration settings via standard REST HTTP calls to the Django views.
*   **WebSocket Connection:** Upon loading, the UI establishes a WebSocket connection to the Daphne server to listen for live updates.
*   **Dynamic Rendering:** As the UI receives JSON payloads from the backend stream, it dynamically updates charts, tables, or log viewers without requiring a page refresh.


