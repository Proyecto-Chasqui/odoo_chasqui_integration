
# Chasqui Integration Module for Odoo

## Overview

This module integrates Odoo with Chasqui, an online sales platform, allowing for seamless synchronization of products and partners between Odoo and Chasqui. It extends the `product.template`, `product.product`, and `res.partner` models to include fields necessary for managing the integration, such as external IDs and sale flags.

## Features

- Adds `external_sale_ok` and `external_product_id` fields to `product.template` and `product.product` models for managing product synchronization.
- Adds `external_partner_id` to the `res.partner` model to manage partner synchronization.
- Automated synchronization of product and partner data between Odoo and Chasqui.

## Prerequisites

- Odoo 16 or later.

## Installation

1. Clone or download the module into your Odoo addons directory.
   ```
   cd /path/to/your/odoo/addons
   git clone https://github.com/Proyecto-Chasqui/odoo_chasqui_integration.git
   ```
2. Update the Odoo addons list by navigating to Apps > Update Apps List in the Odoo backend.
3. Install the module by searching for "Chasqui Integration" in the Apps menu and clicking the Install button.

## Usage

- **Product Synchronization**: To synchronize a product with Chasqui, ensure the `external_sale_ok` flag is set to True on the product form, and specify the `external_product_id`.
- **Partner Synchronization**: To synchronize a partner with Chasqui, fill in the `external_partner_id` field on the partner form.

## Contributing

We welcome contributions! If you have suggestions or want to contribute code, please feel free to submit an issue or pull request on our repository.

## License

This module is licensed under the AGPL-3.0 license. See the LICENSE file for details.
