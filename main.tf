terraform {
    required_providers{
        supabase = {
            source = "supabase/supabase"
            version = "~> 1.0"
        }
    }
}

provider "supabase" {
    api_key = var.supabase_api_key
}

variable "supabase_api_key" {
    type        = string
    description = "The access token for your Supabase account"
    sensitive   = true
}

resource "supabase_project" "market_pipeline" {
    organization_id = var.supabase_org_id
    name    = "ph-market-pipeline-infra"
    region  = "ap-southeast-1" 

    database_config = {
        password = var.db_password
    }
}

variable "supabase_org_id" {
    type        = string
    sensitive   = true
}
