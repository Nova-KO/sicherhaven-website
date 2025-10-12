# PHP Setup for Sicherhaven Template

## Overview
This template has been converted to use PHP includes for common header and footer components, making it easier to maintain and update across all pages.

## Files Created

### PHP Include Files
- `includes/header.php` - Common header with navigation, meta tags, and CSS
- `includes/footer.php` - Common footer with copyright and links

### PHP Pages
- `index.php` - Homepage with Sicherhaven content
- `about.php` - About page with company information

## How It Works

### Header Include (`includes/header.php`)
Contains:
- HTML head section with meta tags
- Page title and description variables
- CSS styles and fonts
- Navigation header
- Opening body and page wrapper tags

### Footer Include (`includes/footer.php`)
Contains:
- Footer content with copyright
- Closing divs and body/html tags

### Page Structure
Each PHP page follows this pattern:
```php
<?php
// Set page-specific variables
$page_title = 'Page Title';
$page_description = 'Page description';

// Include common header
include 'includes/header.php';
?>

<!-- Page-specific content goes here -->

<?php
// Include common footer
include 'includes/footer.php';
?>
```

## Running the PHP Server

### Method 1: Using PHP Built-in Server
```bash
cd "/Users/anjali/Downloads/Sicherhaven Template"
php -S localhost:8001
```

### Method 2: Using a Web Server
You can also use Apache, Nginx, or any other web server that supports PHP.

## Available Pages
- http://localhost:8001/index.php - Homepage
- http://localhost:8001/about.php - About page

## Benefits of This Setup

1. **Maintainability**: Update header/footer in one place, changes apply to all pages
2. **Consistency**: All pages use the same header and footer structure
3. **SEO**: Easy to manage meta tags and titles per page
4. **Scalability**: Easy to add new pages using the same structure

## Adding New Pages

To add a new page:

1. Create a new PHP file (e.g., `contact.php`)
2. Set page-specific variables:
   ```php
   <?php
   $page_title = 'Contact - Sicherhaven Technologies';
   $page_description = 'Contact us for more information about our solutions';
   include 'includes/header.php';
   ?>
   ```
3. Add your page content
4. Include the footer:
   ```php
   <?php include 'includes/footer.php'; ?>
   ```

## Customizing

### Page Titles and Descriptions
Each page can have custom titles and descriptions by setting the variables before including the header.

### Navigation Links
Update the navigation links in `includes/header.php` to point to your PHP pages instead of HTML files.

### Footer Content
Modify `includes/footer.php` to update footer content, copyright, or links.

## Requirements
- PHP 7.0 or higher
- Web server that supports PHP (or PHP built-in server for development)

## Original HTML Files
The original HTML files (`index.html`, `about.html`) are still available for reference or if you need to serve static HTML instead of PHP.
