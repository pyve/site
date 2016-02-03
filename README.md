PyVe Site.
===

On this branch you will find all the set of content to manage the PyVE Site.

Reasons because a module can be here.
---

1. Is a new content for pyve.
2. Is an improvement to the theme for PyVe.
3. Is a Tool to manage such site.

**If you are not on 1, 2 or 3:** please create a website_* module in the [OCA](https://github.com/OCA).

CI Status. | [![Build Status](https://travis-ci.org/pyve/site.svg)](https://travis-ci.org/pyve/site) |
---

Test alive last changes online.

[![Build Status](http://runbot.odoo.com/logo.png)](http://runbot.pyve.com/runbot/team/pyve-25)



This tests is what I need "only" tested/mixed with dependency repositories, and tested 1 by 1 modules on this repository in order to be sure they are all installables.


TODO: Build Status.


Repositories which we depend from.
---

| Repository                 | Travis  | Shippable | Coveral  | Runbot  |
|----------------------------|------|------|-------|----------|---------|
| odoo/odoo                  | N/A  | WIP  | WIP   | WIP      |         |
| pyve/addons-vauxoo         | WIP  | WIP  | WIP   | WIP      |         |

Hacking Our Website
---

Every module can work independent or not, you can find the app installer on [this repository](https://github.com/pyve/site),
please check the [README](https://github.com/pyve/site/blob/9.0/README.md) file there for more precise information.

The main idea is create a little how-to commit by commit to know how create our own features, website features and services offers in a clean way.

For more documentation about "How to do things on Odoo" please refer the [official documentation](https://www.odoo.com/documentation/9.0/) for such tool, this is only an Odoo Module.

How add a new features:
---

0. Clone this repository:

    ```bash
    $ git clone git@github.com:pyve/site.git -b 9.0
    $ cd site
    $ git remote add pyve-dev git@github.com:pyve-dev/site.git # << to push your changes
    ```

1. Install all odoo's dependencies (read travis folder and the requirements.txt file for more information).
**note**: You will need some non normal packages (npm and lessc to be precise) when you have v9.0 normally installed,
run this command in order to have them all in linux and avoid unexpected runtimes.

2. Create your own branch locally.

    ```bash
    $ git checkout -b 9.0-your_new_feature_theme
    ```

3. Push your first change branch to know you start to work on. **note**: remember if you are using a remote personal do
not use origen use your_remote instead.

    ```bash
    $ git push -u origin 9.0-your_new_feature_theme
    ```

4. Prepare your enviroment to work with this repository and the mandatory ones to have all the enviroment ready.

    ```bash
    $ git clone https://github.com/odoo/odoo.git -b 9.0
    $ git clone https://github.com/pyve/site.git -b 9.0
    ```

5. Create a postgres user (only for this work to avoid problems not related to this enviroment).

    ```bash
    $ sudo su postgres
    $ createuser siteuser -P
    # put your password just (1) for example.
    $ createdb site -U siteuser -O siteuser -T remplate0 -E UTF8
    ```

6. Run the development enviroment.

    ```bash
    $ cd path/to/odoo/odoo
    $ ./openerp-server --addons-path=addons/,../site -r \
    siteuser -w 1 --db-filter=site \
    -i www_pyve_com -d site
    ```

7. Do your code, and update it passing -u module -d site (replacing this paramenter above).

8. Before be sure all is ok, we can delete and create db again with -i
   paramenter to ensure all install correctly.

    ```bash
    $ sudo su postgres
    $ dropbd site
    $ createdb site -U siteuser -O siteuser -T remplate0 -E UTF8
    $ ./openerp-server --addons-path=addons/,../site -r \
    siteuser -w 1 --db-filter=site \
    -i www_pyve_com -d site
    ```

9. If all is ok installing, please test your enviroment running your code with ‘test-enabled’.

    ```bash
    $ ./openerp-server --addons-path=addons/,../site -r \
    siteuser -w 1 --db-filter=site \
    -i www_pyve_com -d site --test-enable
    ```

**Note:**

    This will take a time, just do it before commit your change and make push.

10. Add your changes to have them versioned.

    ```bash
    $ git add .
    ```

11. Commit your changes.

    ```bash
    $ git commit -m "[TAG] module: what you did"
    ```

12. Push your first change branch to know you start to work on.

    ```bash
    $ git push -u pyve-dev 9.0-your_new_feature_theme
    ```

13. Make a PR with your changes as you usually do it with graphical interface or using [hub](https://github.com/github/hub).
