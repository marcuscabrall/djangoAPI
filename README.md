# Django REST API Project

This project is a Django-based REST API developed for study purposes. It allows basic CRUD operations on a `User` model, including retrieving, creating, updating, and deleting user data. Testing is conducted using **Postman** to interact with the API endpoints.

## Project Structure

- **Views (`views.py`)**: 
  - `get_users`: Retrieves a list of all users.
  - `get_user_by_nick`: Retrieves or updates a user by nickname.
  - `user_manager`: Manages user creation, retrieval by nickname (via GET query parameter), update, and deletion.

- **URLs (`urls.py`)**: Routes URLs to the corresponding views:
  - `/api/`: Lists all users.
  - `/api/user/<str:nick>`: Retrieves and updates users by nickname.
  - `/api/data/`: Supports CRUD operations on users.

- **Serializers (`serializers.py`)**: 
  - Defines `UserSerializer` for handling `User` data serialization.

- **Admin (`admin.py`)**: 
  - Registers the `User` model in the Django admin panel for easier management during development.

- **Settings (`settings.py`)**: 
  - Configures installed apps, middleware, and the SQLite database used for development.

## API Endpoints

### User Endpoints

1. **Get All Users**  
   - **URL**: `/api/`
   - **Method**: `GET`
   - **Description**: Retrieves a list of all users in the database.

2. **Get User by Nickname**  
   - **URL**: `/api/user/<str:nick>`
   - **Method**: `GET`
   - **Description**: Retrieves a user based on their nickname.

3. **Manage User Data**  
   - **URL**: `/api/data/`
   - **Methods**: `GET`, `POST`, `PUT`, `DELETE`
   - **Description**:
     - `GET`: Retrieves a specific user using the `user` query parameter (e.g., `/api/data/?user=<nickname>`).
     - `POST`: Creates a new user with the provided data.
     - `PUT`: Updates an existing user's information.
     - `DELETE`: Deletes a user based on the provided nickname.

## Testing

The endpoints are tested using **Postman**, allowing the testing of different request methods (GET, POST, PUT, DELETE) with JSON payloads to ensure accurate API functionality and error handling.

## Usage Examples

To use this API, you can test the following example requests:

# Retrieve All Users
```http
GET /api/
```

# Retrieve User by Nickname
```http
GET /api/user/<nickname>
```

# Create New User
```http
POST /api/data/
Content-Type: application/json

{
  "user_nickname": "newuser",
  "email": "newuser@example.com",
  "name": "New User"
}
```

# Update User
```http
PUT /api/data/
Content-Type: application/json

{
  "user_nickname": "existinguser",
  "email": "updated@example.com",
  "name": "Updated Name"
}
```

# Delete User
```http
DELETE /api/data/
Content-Type: application/json

{
  "user_nickname": "userToDelete"
}
```