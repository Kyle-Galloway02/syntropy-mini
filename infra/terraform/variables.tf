variable "pg_user"      { type = string  default = "app" }
variable "pg_password"  { type = string  default = "app" }
variable "pg_db"        { type = string  default = "appdb" }
variable "cors_origin"  { type = string  default = "http://localhost:5173" }
variable "jwt_secret"   { type = string  default = "dev-secret-change-me" }

output "env_file" {
  value = "${path.root}/.env"
}
