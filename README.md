This system will detect the online reachability of servers

Functions
  - MySQL Database
  - Email and SMS notification abilities
  - Create log entry of offline services
  - Service Types
    - HTTP
    - Ping
    - Database
    - Port Scan
    - Mail Server
    - DNS


TODO
  - MySQL integration
  - Latency Warning


Database Columns:
  - service_id      -   int (ai)
  - service_name    -   text
  - service_type    -   text
  - service_address -   text
  - last_checked_status - boolean
  - notification_email  - boolean
  - notification_sms    - boolean
  - email           - text
  - phone_number    - text
