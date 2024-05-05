cat <<EOF > README.md
# Vendor Management System

## Description
The Vendor Management System is a Python project designed to manage vendors' information efficiently.

## Installation
To set up the project locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone git@github.com:dipikanikam/vendor_management.git
   ```

2. Navigate to the project directory:
  ```bash
   cd vendor_management
   ```

3. Create a virtual environment (optional but recommended):
  ```bash
   python3 -m venv venv
   ```

4. Activate the virtual environment:
   - On macOS and Linux:
     ```bash
     source venv/bin/activate
     ```
   - On Windows (Command Prompt):
     ```bash
     venv\\Scripts\\activate.bat
     ```
   - On Windows (PowerShell):
     ```bash
     .\\venv\\Scripts\\Activate.ps1
     ```

5. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

6. Run the application:
   \`\`\`bash
   python app.py
   \`\`\`

7. Open a web browser and navigate to http://localhost:8000 to access the application.

## API Endpoints
- **Vendor List/Create:** `/api/vendors/`
- **Vendor Detail:** `/api/vendors/<int:vendor_id>/`
- **Purchase Order List/Create:** `/api/purchase_orders/`
- **Purchase Order Detail:** `/api/purchase_orders/<int:po_id>/`
- **Vendor Performance:** `/api/vendors/<int:vendor_id>/performance/`

## Usage
- Upon accessing the application, you will be able to manage vendors' information efficiently through the user-friendly interface.

## Usage
- Upon accessing the application, you will be able to manage vendors' information efficiently through the user-friendly interface.

## Contributing
Contributions are welcome! Please follow these steps to contribute to the project:
1. Fork the repository.
2. Create a new branch (\`git checkout -b feature/new-feature\`).
3. Make your changes.
4. Commit your changes (\`git commit -am 'Add new feature'\`).
5. Push to the branch (\`git push origin feature/new-feature\`).
6. Create a new Pull Request.

## Postman collection 

https://documenter.getpostman.com/view/34713823/2sA3JGfPRo