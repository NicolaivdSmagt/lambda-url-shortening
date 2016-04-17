# Lambda URL Shortener compatible with Tweetbot URL shortening

This repo contains components for a URL shortner service running on Amazon's API Gateway and Lambda services. It is compatible with most applications that can use URL shortening automatically, such as Tweetbot.

## Components

* API Gateway front-end
* Lambda Python function back-end
* DynamoDB datastore

### Required AWS resources

The `main.tf` [Terraform](https://www.terraform.io/) file contains basic resources required for DynamoDB including a table and IAM role with associated policies.

To use this [install and configure Terraform](https://www.terraform.io/intro/getting-started/install.html) for your AWS account.

### API Gateway

[redir-v2-swagger.json](redir-v2-swagger.json) contains a [Swagger](http://swagger.io/getting-started/) JSON definition for the front-end interface. This can be imported into your AWS using Amazon's [API Gateway Importer](https://github.com/awslabs/aws-apigateway-importer).

**NOTE**: References to Amazon account id have been replaced with `{{YOUR AWS ACCOUNT ID}}`. You will need to change these to your numeric AWS account id.

### Lambda Functions

All Lambda functions are organized under `lambda` using the [Apex framework](http://apex.run/).

**NOTE**: References to Amazon account id have been replaced with `{{YOUR AWS ACCOUNT ID}}`. You will need to change these to your numeric AWS account id. Also, pick a simple password for authentication {{PASS}}.

Once you [install Apex](http://apex.run/#installation), you can deploy via the CLI:

```
> cd lambda
> apex deploy
```

And execute locally via the CLI:

```
> cd lambda
> echo '{ "token":"xxxxxxx" }' | apex invoke lookup_token
```
To configure URL shortening in Tweetbot, go to preferences and configure "custom" URL shortening. For the API endpoint, use: "https://{{YOURDOMAIN}}/?auth={{PASS}}&url=%@".
