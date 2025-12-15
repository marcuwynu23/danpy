"""
Tests for DAN (Data Advanced Notation) Parser and Encoder
"""

import unittest
import sys
import os

# Add parent directory to path to import dan module
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from dan import decode, encode


class TestDANDecode(unittest.TestCase):
    """Test cases for decode function"""
    
    def test_empty_string(self):
        """Test decoding empty string"""
        result = decode("")
        self.assertEqual(result, {})
    
    def test_empty_string_with_whitespace(self):
        """Test decoding string with only whitespace"""
        result = decode("   \n  \t  ")
        self.assertEqual(result, {})
    
    def test_simple_key_value(self):
        """Test simple key-value pair"""
        text = "name: John"
        result = decode(text)
        self.assertEqual(result, {"name": "John"})
    
    def test_string_with_quotes(self):
        """Test quoted string value"""
        text = 'name: "John Doe"'
        result = decode(text)
        self.assertEqual(result, {"name": "John Doe"})
    
    def test_boolean_values(self):
        """Test boolean values"""
        text = "active: true\nenabled: false"
        result = decode(text)
        self.assertEqual(result, {"active": True, "enabled": False})
    
    def test_numeric_values(self):
        """Test numeric values"""
        text = "age: 25\nprice: 99.99\ncount: 100"
        result = decode(text)
        self.assertEqual(result, {"age": 25, "price": 99.99, "count": 100})
    
    def test_array_values(self):
        """Test array values"""
        text = 'roles: [admin, user, guest]'
        result = decode(text)
        self.assertEqual(result, {"roles": ["admin", "user", "guest"]})
    
    def test_empty_array(self):
        """Test empty array"""
        text = "items: []"
        result = decode(text)
        self.assertEqual(result, {"items": []})
    
    def test_nested_blocks(self):
        """Test nested block structures"""
        text = """
app {
  name: "MyApp"
  server {
    host: localhost
    port: 3000
  }
}
"""
        result = decode(text)
        self.assertEqual(result, {
            "app": {
                "name": "MyApp",
                "server": {
                    "host": "localhost",
                    "port": 3000
                }
            }
        })
    
    def test_table(self):
        """Test table structure"""
        text = """
users: table(id, username, email) [
  1, alice, "alice@example.com"
  2, bob, "bob@example.com"
]
"""
        result = decode(text)
        self.assertEqual(result, {
            "users": [
                {"id": 1, "username": "alice", "email": "alice@example.com"},
                {"id": 2, "username": "bob", "email": "bob@example.com"}
            ]
        })
    
    def test_table_with_mixed_types(self):
        """Test table with mixed data types"""
        text = """
users: table(id, username, active, score) [
  1, alice, true, 95.5
  2, bob, false, 87.0
]
"""
        result = decode(text)
        self.assertEqual(result, {
            "users": [
                {"id": 1, "username": "alice", "active": True, "score": 95.5},
                {"id": 2, "username": "bob", "active": False, "score": 87.0}
            ]
        })
    
    def test_comments_hash(self):
        """Test comments with #"""
        text = """
# This is a comment
name: John  # Inline comment
age: 25
"""
        result = decode(text)
        self.assertEqual(result, {"name": "John", "age": 25})
    
    def test_comments_double_slash(self):
        """Test comments with //"""
        text = """
// This is a comment
name: John  // Inline comment
age: 25
"""
        result = decode(text)
        self.assertEqual(result, {"name": "John", "age": 25})
    
    def test_comments_both_types(self):
        """Test comments with both # and //"""
        text = """
# Comment 1
name: John  // Comment 2
age: 25  # Comment 3
"""
        result = decode(text)
        self.assertEqual(result, {"name": "John", "age": 25})
    
    def test_bytes_input(self):
        """Test decoding bytes input"""
        text_bytes = b'name: "John"\nage: 25'
        result = decode(text_bytes)
        self.assertEqual(result, {"name": "John", "age": 25})
    
    def test_invalid_input_type(self):
        """Test invalid input type raises TypeError"""
        with self.assertRaises(TypeError):
            decode(123)
    
    def test_sample_file(self):
        """Test with the provided sample.dan file"""
        sample_text = """# Sample DAN configuration file
# This demonstrates various DAN features

app {
  name: "Sample Application"
  version: 1.0.0
  environment: production

  # Server configuration
  server {
    host: localhost
    port: 3000
    ssl: false
  }

  # Database settings
  database {
    type: postgresql
    host: db.example.com
    port: 5432
    name: myapp
  }
}

# Feature flags
features {
  authentication: true
  analytics: false
  logging: true
}

# User roles
roles: [admin, user, guest]

# Application users
users: table(id, username, email, role, active) [
  1, alice, "alice@example.com", admin, true
  2, bob, "bob@example.com", user, true
  3, charlie, "charlie@example.com", guest, false
]

# API endpoints
endpoints: table(method, path, handler, auth) [
  GET, "/api/users", getUsers, true
  POST, "/api/users", createUser, true
  GET, "/api/public", getPublic, false
]
"""
        result = decode(sample_text)
        
        # Verify structure
        self.assertIn("app", result)
        self.assertIn("features", result)
        self.assertIn("roles", result)
        self.assertIn("users", result)
        self.assertIn("endpoints", result)
        
        # Verify app block
        self.assertEqual(result["app"]["name"], "Sample Application")
        self.assertEqual(result["app"]["version"], "1.0.0")  # Version strings remain as strings
        self.assertEqual(result["app"]["server"]["port"], 3000)
        
        # Verify features
        self.assertTrue(result["features"]["authentication"])
        self.assertFalse(result["features"]["analytics"])
        
        # Verify roles array
        self.assertEqual(result["roles"], ["admin", "user", "guest"])
        
        # Verify users table
        self.assertEqual(len(result["users"]), 3)
        self.assertEqual(result["users"][0]["username"], "alice")
        self.assertEqual(result["users"][0]["email"], "alice@example.com")
        self.assertTrue(result["users"][0]["active"])
        
        # Verify endpoints table
        self.assertEqual(len(result["endpoints"]), 3)
        self.assertEqual(result["endpoints"][0]["method"], "GET")
        self.assertEqual(result["endpoints"][0]["path"], "/api/users")


class TestDANEncode(unittest.TestCase):
    """Test cases for encode function"""
    
    def test_empty_dict(self):
        """Test encoding empty dictionary"""
        result = encode({})
        self.assertEqual(result, "")
    
    def test_simple_key_value(self):
        """Test encoding simple key-value pair"""
        obj = {"name": "John"}
        result = encode(obj)
        self.assertEqual(result, 'name: "John"')
    
    def test_boolean_values(self):
        """Test encoding boolean values"""
        obj = {"active": True, "enabled": False}
        result = encode(obj)
        self.assertIn("active: true", result)
        self.assertIn("enabled: false", result)
    
    def test_numeric_values(self):
        """Test encoding numeric values"""
        obj = {"age": 25, "price": 99.99}
        result = encode(obj)
        self.assertIn("age: 25", result)
        self.assertIn("price: 99.99", result)
    
    def test_array_values(self):
        """Test encoding array values"""
        obj = {"roles": ["admin", "user", "guest"]}
        result = encode(obj)
        self.assertEqual(result, 'roles: ["admin", "user", "guest"]')
    
    def test_empty_array(self):
        """Test encoding empty array"""
        obj = {"items": []}
        result = encode(obj)
        self.assertEqual(result, "items: []")
    
    def test_nested_blocks(self):
        """Test encoding nested blocks"""
        obj = {
            "app": {
                "name": "MyApp",
                "server": {
                    "host": "localhost",
                    "port": 3000
                }
            }
        }
        result = encode(obj)
        self.assertIn("app {", result)
        self.assertIn('name: "MyApp"', result)
        self.assertIn("server {", result)
        self.assertIn("host: \"localhost\"", result)
        self.assertIn("port: 3000", result)
        self.assertIn("}", result)
    
    def test_table(self):
        """Test encoding table structure"""
        obj = {
            "users": [
                {"id": 1, "username": "alice", "email": "alice@example.com"},
                {"id": 2, "username": "bob", "email": "bob@example.com"}
            ]
        }
        result = encode(obj)
        self.assertIn("users: table(id, username, email) [", result)
        self.assertIn('1, "alice", "alice@example.com"', result)
        self.assertIn('2, "bob", "bob@example.com"', result)
        self.assertIn("]", result)
    
    def test_table_with_mixed_types(self):
        """Test encoding table with mixed data types"""
        obj = {
            "users": [
                {"id": 1, "username": "alice", "active": True, "score": 95.5},
                {"id": 2, "username": "bob", "active": False, "score": 87.0}
            ]
        }
        result = encode(obj)
        self.assertIn("users: table(id, username, active, score) [", result)
        self.assertIn('1, "alice", true, 95.5', result)
        self.assertIn('2, "bob", false, 87.0', result)
    
    def test_round_trip(self):
        """Test encode/decode round trip"""
        original = {
            "app": {
                "name": "MyApp",
                "version": 1.0,
                "server": {
                    "host": "localhost",
                    "port": 3000,
                    "ssl": False
                }
            },
            "features": {
                "auth": True,
                "logging": False
            },
            "roles": ["admin", "user"],
            "users": [
                {"id": 1, "name": "Alice", "active": True},
                {"id": 2, "name": "Bob", "active": False}
            ]
        }
        
        encoded = encode(original)
        decoded = decode(encoded)
        
        self.assertEqual(decoded, original)
    
    def test_round_trip_with_sample(self):
        """Test round trip with sample data similar to sample.dan"""
        original = {
            "app": {
                "name": "Sample Application",
                "version": 1.0,
                "environment": "production",
                "server": {
                    "host": "localhost",
                    "port": 3000,
                    "ssl": False
                },
                "database": {
                    "type": "postgresql",
                    "host": "db.example.com",
                    "port": 5432,
                    "name": "myapp"
                }
            },
            "features": {
                "authentication": True,
                "analytics": False,
                "logging": True
            },
            "roles": ["admin", "user", "guest"],
            "users": [
                {"id": 1, "username": "alice", "email": "alice@example.com", "role": "admin", "active": True},
                {"id": 2, "username": "bob", "email": "bob@example.com", "role": "user", "active": True},
                {"id": 3, "username": "charlie", "email": "charlie@example.com", "role": "guest", "active": False}
            ],
            "endpoints": [
                {"method": "GET", "path": "/api/users", "handler": "getUsers", "auth": True},
                {"method": "POST", "path": "/api/users", "handler": "createUser", "auth": True},
                {"method": "GET", "path": "/api/public", "handler": "getPublic", "auth": False}
            ]
        }
        
        encoded = encode(original)
        decoded = decode(encoded)
        
        self.assertEqual(decoded, original)


class TestDANEdgeCases(unittest.TestCase):
    """Test edge cases and special scenarios"""
    
    def test_unquoted_strings(self):
        """Test unquoted string values"""
        text = "host: localhost\nport: 3000"
        result = decode(text)
        self.assertEqual(result["host"], "localhost")
        self.assertEqual(result["port"], 3000)
    
    def test_array_with_numbers(self):
        """Test array with numeric values"""
        text = "numbers: [1, 2, 3, 4, 5]"
        result = decode(text)
        self.assertEqual(result["numbers"], [1, 2, 3, 4, 5])
    
    def test_array_with_mixed_types(self):
        """Test array with mixed types"""
        text = 'mixed: [1, "two", true, false, 3.14]'
        result = decode(text)
        self.assertEqual(result["mixed"], [1, "two", True, False, 3.14])
    
    def test_table_with_empty_values(self):
        """Test table handling"""
        text = """
data: table(col1, col2) [
  val1, val2
  val3, val4
]
"""
        result = decode(text)
        self.assertEqual(len(result["data"]), 2)
    
    def test_deeply_nested_blocks(self):
        """Test deeply nested block structures"""
        text = """
level1 {
  level2 {
    level3 {
      value: test
    }
  }
}
"""
        result = decode(text)
        self.assertEqual(result["level1"]["level2"]["level3"]["value"], "test")
    
    def test_multiple_tables(self):
        """Test multiple tables in same document"""
        text = """
users: table(id, name) [
  1, Alice
]
products: table(id, name, price) [
  1, Widget, 9.99
]
"""
        result = decode(text)
        self.assertIn("users", result)
        self.assertIn("products", result)
        self.assertEqual(len(result["users"]), 1)
        self.assertEqual(len(result["products"]), 1)


class TestDANScenarios(unittest.TestCase):
    """Additional test scenarios for real-world use cases"""
    
    def test_config_file_scenario(self):
        """Test configuration file scenario"""
        config = """
# Application Configuration
app {
  name: "My Application"
  version: 2.1.0
  debug: false
  
  logging {
    level: info
    file: "app.log"
    max_size: 10485760
  }
  
  cache {
    enabled: true
    ttl: 3600
    max_entries: 1000
  }
}
"""
        result = decode(config)
        self.assertEqual(result["app"]["name"], "My Application")
        self.assertEqual(result["app"]["debug"], False)
        self.assertEqual(result["app"]["logging"]["level"], "info")
        self.assertEqual(result["app"]["cache"]["ttl"], 3600)
    
    def test_database_schema_scenario(self):
        """Test database schema scenario"""
        schema = """
# Database Schema
tables: table(name, columns, primary_key) [
  users, "id, username, email", id
  posts, "id, title, content, user_id", id
  comments, "id, post_id, content, user_id", id
]

relationships: table(from_table, to_table, type, foreign_key) [
  posts, users, many_to_one, user_id
  comments, posts, many_to_one, post_id
  comments, users, many_to_one, user_id
]
"""
        result = decode(schema)
        self.assertEqual(len(result["tables"]), 3)
        self.assertEqual(len(result["relationships"]), 3)
        self.assertEqual(result["tables"][0]["name"], "users")
    
    def test_api_routes_scenario(self):
        """Test API routes scenario"""
        routes = """
# API Routes Configuration
routes: table(method, path, controller, action, middleware) [
  GET, "/api/users", UserController, index, "auth, admin"
  GET, "/api/users/:id", UserController, show, auth
  POST, "/api/users", UserController, create, "auth, admin"
  PUT, "/api/users/:id", UserController, update, "auth, admin"
  DELETE, "/api/users/:id", UserController, destroy, "auth, admin"
]

middleware {
  auth: "AuthMiddleware"
  admin: "AdminMiddleware"
  rate_limit: "RateLimitMiddleware"
}
"""
        result = decode(routes)
        self.assertEqual(len(result["routes"]), 5)
        self.assertEqual(result["routes"][0]["method"], "GET")
        self.assertEqual(result["middleware"]["auth"], "AuthMiddleware")
    
    def test_game_config_scenario(self):
        """Test game configuration scenario"""
        game_config = """
# Game Configuration
game {
  title: "Adventure Quest"
  version: 1.5.2
  
  player {
    max_health: 100
    starting_level: 1
    experience_curve: [100, 250, 500, 1000, 2000]
  }
  
  items: table(id, name, type, value, rarity) [
    1, "Sword", weapon, 50, common
    2, "Shield", armor, 30, common
    3, "Health Potion", consumable, 20, common
    4, "Dragon Scale", material, 500, legendary
  ]
  
  enemies: table(id, name, health, damage, experience) [
    1, Goblin, 30, 5, 10
    2, Orc, 60, 10, 25
    3, Dragon, 200, 30, 100
  ]
}
"""
        result = decode(game_config)
        self.assertEqual(result["game"]["title"], "Adventure Quest")
        self.assertEqual(len(result["game"]["items"]), 4)
        self.assertEqual(len(result["game"]["enemies"]), 3)
        self.assertEqual(result["game"]["player"]["max_health"], 100)
    
    def test_ci_cd_config_scenario(self):
        """Test CI/CD configuration scenario"""
        cicd = """
# CI/CD Pipeline Configuration
pipeline {
  name: "Build and Deploy"
  
  stages: table(name, commands, parallel) [
    build, "npm install, npm run build", false
    test, "npm test, npm run lint", false
    deploy_staging, "deploy.sh staging", false
    deploy_prod, "deploy.sh production", true
  ]
  
  environments {
    staging {
      url: "https://staging.example.com"
      auto_deploy: true
    }
    production {
      url: "https://example.com"
      auto_deploy: false
      requires_approval: true
    }
  }
  
  notifications {
    slack: true
    email: false
    webhook: "https://hooks.example.com/ci"
  }
}
"""
        result = decode(cicd)
        self.assertEqual(len(result["pipeline"]["stages"]), 4)
        self.assertEqual(result["pipeline"]["environments"]["staging"]["auto_deploy"], True)
        self.assertEqual(result["pipeline"]["notifications"]["slack"], True)
    
    def test_microservices_config_scenario(self):
        """Test microservices configuration scenario"""
        services = """
# Microservices Configuration
services: table(name, port, version, dependencies) [
  auth-service, 3001, 1.2.0, "[]"
  user-service, 3002, 2.0.1, "[auth-service]"
  order-service, 3003, 1.5.0, "[auth-service, user-service]"
  payment-service, 3004, 1.0.0, "[auth-service, order-service]"
]

gateway {
  port: 8080
  routes: table(service, path, methods) [
    auth-service, "/api/auth", "[POST, GET]"
    user-service, "/api/users", "[GET, POST, PUT, DELETE]"
    order-service, "/api/orders", "[GET, POST, PUT]"
    payment-service, "/api/payments", "[POST, GET]"
  ]
}
"""
        result = decode(services)
        self.assertEqual(len(result["services"]), 4)
        self.assertEqual(result["services"][0]["port"], 3001)
        self.assertEqual(len(result["gateway"]["routes"]), 4)
    
    def test_round_trip_complex_scenario(self):
        """Test round trip with complex nested scenario"""
        original = {
            "application": {
                "name": "Complex App",
                "modules": {
                    "auth": {
                        "enabled": True,
                        "providers": ["local", "oauth", "ldap"]
                    },
                    "database": {
                        "type": "postgresql",
                        "pool_size": 10
                    }
                },
                "features": ["feature1", "feature2", "feature3"],
                "users": [
                    {"id": 1, "name": "Alice", "role": "admin"},
                    {"id": 2, "name": "Bob", "role": "user"}
                ]
            }
        }
        
        encoded = encode(original)
        decoded = decode(encoded)
        
        self.assertEqual(decoded, original)


if __name__ == "__main__":
    unittest.main()

