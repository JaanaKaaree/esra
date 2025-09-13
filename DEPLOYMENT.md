# ESRA Website Deployment Guide

## Overview
This repository includes an automated GitHub Actions workflow that deploys the website to AWS S3 and invalidates CloudFront when files in the `output/` directory are updated.

## Workflow Features

### Trigger Conditions
- **Automatic**: Triggers on pushes to `main` branch when files in `output/` directory change
- **Manual**: Can be triggered manually via GitHub Actions UI

### What It Does
1. **Detects Changes**: Identifies which files were modified in the `output/` directory
2. **S3 Sync**: Uploads changed files to S3 bucket with appropriate cache headers
3. **CloudFront Invalidation**: Invalidates CloudFront cache for changed files
4. **Smart Caching**: 
   - Static assets (CSS, JS, images): 1 year cache
   - HTML/XML files: 1 hour cache

## Required GitHub Secrets

You need to configure the following secrets in your GitHub repository:

### 1. AWS Access Credentials
- `AWS_ACCESS_KEY_ID`: Your AWS access key ID
- `AWS_SECRET_ACCESS_KEY`: Your AWS secret access key
- `AWS_REGION`: AWS region (e.g., `us-east-1`, `ap-southeast-2`)

### 2. S3 Configuration
- `S3_BUCKET_NAME`: Your S3 bucket name (e.g., `esra.co.nz`)

### 3. CloudFront Configuration
- `CLOUDFRONT_DISTRIBUTION_ID`: Your CloudFront distribution ID

## How to Set Up Secrets

1. Go to your GitHub repository
2. Click **Settings** → **Secrets and variables** → **Actions**
3. Click **New repository secret**
4. Add each secret with the exact name and value

## AWS IAM Permissions

Your AWS user/role needs the following permissions:

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "s3:GetObject",
                "s3:PutObject",
                "s3:DeleteObject",
                "s3:ListBucket",
                "s3:PutObjectAcl"
            ],
            "Resource": [
                "arn:aws:s3:::esra.co.nz",
                "arn:aws:s3:::esra.co.nz/*"
            ]
        },
        {
            "Effect": "Allow",
            "Action": [
                "cloudfront:CreateInvalidation",
                "cloudfront:GetInvalidation",
                "cloudfront:ListInvalidations"
            ],
            "Resource": "arn:aws:cloudfront::*:distribution/*"
        }
    ]
}
```

## S3 Bucket Configuration

Ensure your S3 bucket has:
- **Static website hosting** enabled
- **Public read access** for website files
- **CORS configuration** if needed

## CloudFront Configuration

Your CloudFront distribution should:
- Have the S3 bucket as origin
- Be configured for static website hosting
- Have appropriate cache behaviors

## Workflow Files

- `.github/workflows/deploy-to-s3.yml`: Main deployment workflow

## Testing the Deployment

1. Make changes to files in the `output/` directory
2. Commit and push to `main` branch
3. Check GitHub Actions tab for deployment status
4. Visit your website to verify changes

## Manual Deployment

You can trigger deployment manually:
1. Go to **Actions** tab in GitHub
2. Select **Deploy to S3 and CloudFront** workflow
3. Click **Run workflow**
4. Select branch and click **Run workflow**

## Troubleshooting

### Common Issues
- **Permission denied**: Check AWS credentials and IAM permissions
- **Bucket not found**: Verify S3 bucket name in secrets
- **CloudFront invalidation failed**: Check distribution ID and permissions
- **Files not uploading**: Verify file paths and S3 bucket configuration

### Logs
Check the GitHub Actions logs for detailed error messages and troubleshooting information.
