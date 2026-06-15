# 1. Tell Terraform we want to connect to Supabase
terraform {
  required_providers {
    supabase = {
      source  = "supabase/supabase"
      version = "~> 1.0"
    }
  }
}

provider "supabase" {
  access_token = var.supabase_access_token
}


variable "supabase_access_token" {
  type      = string
  sensitive = true
}

variable "supabase_org_id" {
  type      = string
  sensitive = true
}

variable "db_password" {
  type      = string
  sensitive = true
}


resource "supabase_project" "market_pipeline" {
  organization_id   = var.supabase_org_id
  name              = "ph-market-pipeline-infra"
  region            = "ap-southeast-1" # Singapore (closest to PH)
  database_password = var.db_password
}