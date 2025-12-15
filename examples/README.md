# DAN Examples

This directory contains various example DAN files demonstrating different use cases and scenarios.

## Example Files

### Configuration Files
- **sample.dan** - Basic application configuration example
- **config.dan** - Comprehensive application configuration with server, database, logging, and cache settings

### Database & Data
- **database_schema.dan** - Database schema definitions with tables, relationships, and seed data

### API & Web
- **api_routes.dan** - RESTful API route definitions with middleware and rate limiting
- **microservices.dan** - Microservices architecture configuration with service registry and gateway

### Infrastructure
- **docker_compose.dan** - Docker Compose configuration in DAN format
- **kubernetes.dan** - Kubernetes resource definitions (deployments, services, ingress)
- **terraform.dan** - Infrastructure as Code definitions (VPCs, instances, load balancers)
- **cicd_pipeline.dan** - CI/CD pipeline configuration with stages, environments, and notifications

### Development
- **package_manifest.dan** - Package and dependency management
- **monitoring.dan** - Monitoring, logging, and observability configuration

### Specialized
- **game_config.dan** - RPG game configuration with items, enemies, and quests
- **iot_devices.dan** - IoT device management and automation rules
- **security_policy.dan** - Security policies, authentication, and access control
- **ecommerce.dan** - E-commerce platform configuration
- **social_media.dan** - Social media platform settings

## Usage

You can decode any of these example files using the DAN library:

```python
from dan import decode

with open('examples/config.dan', 'r') as f:
    config = decode(f.read())

print(config['app']['name'])
```

## Testing

All example files are tested in the test suite to ensure they can be properly decoded and encoded.

