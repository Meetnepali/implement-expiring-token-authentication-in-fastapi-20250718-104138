# Task Overview
You are supporting an operations-critical FastAPI microservice that powers customer search for the business dashboard. Users have encountered persistent server-side errors on the customer search endpoint, making business operations difficult and blocking customer lookup functionality. The search API is supposed to allow filtering by customer name and active status, but currently returns internal server errors when called.

# Guidance
Review the customer search functionality with attention to how optional query parameters and response models are handled. Examine both the query parameter defaults and the API's response formatting to identify flaws that cause unhelpful errors and failed searches. Retain existing endpoint paths and models while ensuring best practices in filter and output handling are applied.

# Objectives
Restore correct and reliable operation of the customer search capability. Ensure that the endpoint processes optional name and active filters, never fails on missing or absent parameters, and returns a properly structured list of matching customers within a successful 200 OK JSON response. Ensure that OpenAPI documentation accurately reflects usage and that error scenarios return useful, informative messages.

# How to Verify
After deployment, requests to the customer search endpoint should be accepted with or without query parameters and must return a 200 OK status and a structured JSON response listing only the matched customers. The OpenAPI docs should display the endpoint accurately. All searches (including those with missing query parameters) must succeed with a well-formed result, and no internal server errors should occur.