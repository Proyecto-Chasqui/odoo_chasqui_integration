
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

- **Product Synchronization:** The `external_sale_ok` and `external_product_id` fields are added to the `product.template` model. The `external_sale_ok` field indicates whether a product can be sold on Chasqui, while the `external_product_id` is used to identify the product on the Chasqui platform.

- **Partner Synchronization:** The `external_partner_id` field is added to the `res.partner` model. This field is used to manage partner synchronization by uniquely identifying partners across Odoo and Chasqui.

- **Automated Synchronization:** Fields `sync_id`, `sync_hash`, and `sync_timestamp` are included in both `product` and `partner` models to facilitate the synchronization mechanism, ensuring that product and partner data are kept up to date between Odoo and Chasqui.



## Contributing

We welcome contributions! If you have suggestions or want to contribute code, please feel free to submit an issue or pull request on our repository.

## License

This module is licensed under the AGPL-3.0 license. See the LICENSE file for details.
