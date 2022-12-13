<!-- markdownlint-configure-file {
  "MD013": {
    "code_blocks": false,
    "tables": false
  },
  "MD033": false,
  "MD041": false
} -->

[![Stand With Ukraine](https://raw.githubusercontent.com/vshymanskyy/StandWithUkraine/main/banner2-direct.svg)](https://stand-with-ukraine.pp.ua)

<h1 align="center">Strichka UA</h1>

<p align="center">
  <img src="https://i.imgur.com/hsKo6IP.png" alt="Welcome Logo" width="800">
</p>

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

<div align="center">
    <img src="https://forthebadge.com/images/badges/made-with-python.svg"/>
    <img src="https://forthebadge.com/images/badges/check-it-out.svg"/>
    <img src="https://forthebadge.com/images/badges/powered-by-electricity.svg"/>
</div>
<div align="center">
    <img src="https://forthebadge.com/images/badges/made-with-markdown.svg"/>
    <img src="https://forthebadge.com/images/badges/fuck-it-ship-it.svg"/>
    <img src="https://forthebadge.com/images/badges/powered-by-netflix.svg"/>
</div>

<div align="center">
    <h4>
        <img width="13%" src="https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue"/>
        <img width="13%" src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=green"/>
        <img width="18%" src="https://img.shields.io/badge/django%20rest-ff1709?style=for-the-badge&logo=django&logoColor=white"/>
        <img width="17%" src="https://img.shields.io/badge/JavaScript-323330?style=for-the-badge&logo=javascript&logoColor=F7DF1E"/>
        <img width="11%" src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white"/>
    </h4>
</div>


<div align="center">
    <h4>
        <a href="https://docs.python.org/3/whatsnew/3.11.html">
            <img src="https://img.shields.io/badge/Made%20with-Python%203.11-1f425f.svg?logo=python"/>
        </a>
        <a href="https://github.com/pre-commit/pre-commit">
            <img src="https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white&style=flat"/>
        </a>
        <a href="">
            <img src="https://img.shields.io/badge/contributions-welcome-orange.svg"/>
        </a>
        <a href="">
            <img src="https://img.shields.io/badge/PRs-welcome-orange.svg?style=shields"/>
        </a>
    </h4>
</div>
<div align="center">
    <h4>
        <a href="https://github.com/psf/black">
            <img src="https://img.shields.io/badge/code%20style-black-000000.svg"/>
        </a>
        <a href="http://mypy-lang.org/">
            <img src="http://www.mypy-lang.org/static/mypy_badge.svg"/>
        </a>
        <a href="https://pycqa.github.io/isort/">
            <img src="https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336"/>
        </a>
        <a href="">
            <img src="https://img.shields.io/badge/dependencies-up%20to%20date-brightgreen.svg"/>
        </a>
    </h4>
</div>

<div align="center">

[**Description**](#description) •
[**Quickstart**](#quickstart) •
[**Features**](#features) •
[**Supported Platforms**](#platforms) •
[**Stack**](#stack)

</div>

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

<h2 align="center" id="description">📖 Description</h2>

This project is designed to find movies, under the hood it contains a whole variety of different scrapers thanks to which you can find on which platforms a movie is available, so you can conveniently find a movie to watch on your favorite platform.

You can also **register** on the site (with email confirmation), after which you will become a full-fledged user.

Registered users have the opportunity to rate, comment and add movie to the watchlist.

The project is written in **Python 3.11** and **Django 4.1** (latest versions).

The application also has its own **API (REST)** and **Swagger**.

Contains linters for checking code quality, integrated into **GitHub Actions**.

The project has **caching** for almost everything important. Therefore, a quick response will be even faster.

Also, the project is fully **dockerized**.

You can read about all the mentioned and other things further.

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

<h2 align="center" id="quickstart">⚡️ Quickstart</h2>

* Clone the repo.

* Create and activate a python3 virtualenv via your preferred method.

* Install the dependencies. Run:

	```bash
	pip install -r requirements.txt
	```

* Install pre-commit hooks to ensure code quality checks and style checks:

	```bash
	make install_hooks
	```

	* You can also use these commands during dev process:

		* To run **mypy** checks:

			```bash
			make types
			```

		* To run **flake8** checks:

			```bash
			make flake
			```

		* To run **black** checks:

			```bash
			make black
			```

		* To run together:

			```bash
			make lint
			```

* Replace `.env.example` with real `.env`, changing placeholders

	```
	SECRET_KEY=<fill-me>
	DEPLOY_ENVIRONMENT=<stage|prod>

	SITE_ID=<site-id>

	EMAIL_HOST_USER=<email-host-user>
 	EMAIL_HOST_PASSWORD=email-host-password
  	EMAIL_HOST=<email-host>

    DATABASE_URL=<postgres-connection-uri>

    REDIS_HOST=<redis-host>
    REDIS_PASSWORD=<redis-password>
    REDIS_PORT=<redis-port>
    REDIS_DB=<redis-db>
	```

* Export path to Environment Variables:

	```bash
	export PYTHONPATH='.'
	```

* Run following commands to make migrations and create admin user:

	```bash
	make migrate
    make user
	```

* Start the Strichka App:

	* Run server with test settings:

		```bash
		 make runserver-test
		```

	* Run server with dev settings:

		```bash
		 make runserver-dev
		```
	* Run server with prod settings:

		```bash
		 makerunserver-prod
		```

* Alternatively, you can just start Docker:

	```bash
    make docker_build
    ```

* And it's done!

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

<h2 align="center" id="features">✨ Features</h2>

<div align="center">

🔹 [**Scraping and Validation**](#scraping) 🔹
[**REST API + Swagger**](#rest) 🔹
[**Awesome Front-End**](#front) 🔹

</div>

<div align="center">

🔹 [**Admin Panel**](#panel) 🔹
[**Authentication**](#authentication) 🔹
[**Caching**](#caching) 🔹
[**Dockerization**](#dockerization) 🔹
[**Debug Toolbar**](#debug) 🔹

</div>

<h3 align="center" id="scraping">Scraping and Validation</h3>

Data scraping is one of the best features of this project, but due to its uniqueness, certain tricks and a bit of unpreparedness of the code, I did not include this module in this project.

At the moment, my project can find if a movie is available for viewing on **more than 20 platforms**, however, there are still big nuances with updating information, but at the basic level it is supported, at least once a month.

All data that was collected before entering the database is validated through [`Pydantic`](https://docs.pydantic.dev/usage/validators/), similarly, if you want to add a new item through the admin panel, it will also be validated through [`Pydantic`](https://docs.pydantic.dev/usage/validators/) models. See the logic for this in `schema.py`.

Therefore, the data here is clean and beautiful (maybe not all).

<h3 align="center" id="rest">REST API + Swagger</h3>

Another cool feature of this project is the presence of its own API implemented using the [`Django REST API`](https://www.django-rest-framework.org/).

BasicAuthentication is configured for logging into the API. There are also corresponding serializers for each model. Views are implemented on the basis of `ModelViewSet`. `DjangoFilterBackend` from the [`django_filters`](https://django-filter.readthedocs.io/en/stable/guide/usage.html) library is also implemented. This allows us to conveniently filter, sort and search our data. Of course, pagination is also available here.

Swagger was also installed for the project, [`drf_spectacular`](https://drf-spectacular.readthedocs.io/en/latest/) helped.

On the screenshots below, you can see how everything looks. See the `api/` folder and `serializers.py` for more details.

API View         |  API Filters
:-------------------------:|:-------------------------:
<img src="https://i.imgur.com/XgVuSbx.png" title="API View" width="100%"> |<img src="https://i.imgur.com/uquMqM5.png" title="API Filters" width="100%">

API POST Form        |  Swagger
:-------------------------:|:-------------------------:
<img src="https://i.imgur.com/2v3qWEc.png" title="API POST Form" width="100%"> |<img src="https://i.imgur.com/1Lfbe49.png" title="Swagger" width="100%">

<h3 align="center" id="front">Awesome Front-End</h3>

Really, just look at this design, it's beautiful.

Here everything is written in pure `CSS` + `JavaScript`, also using such libraries as `JQuery`, `Bootstrap`, `InfinityScroll` and `Owl`.

I tried to make the design as user-friendly and pleasant as possible, so it supports easily on phones as well.

For more details, see the implementation in the `static`/ and `templates/` folders.

And on the screenshots below you can see all the beauty of my project:

Main Page         |  Movies List  | Movie Page
:-------------------------:|:-------------------------:|:-------------------------:
<img src="https://i.imgur.com/LcL1Zdb.png" title="Main Page" width="100%"> |<img src="https://i.imgur.com/OsJCMiv.png" title="Movies List" width="100%">|<img src="https://i.imgur.com/o8MD5lg.png" title="Movie Page" width="100%">

Movie Page Extra         |  Collection Page   |  Comments
:-------------------------:|:-------------------------:|:-------------------------:
<img src="https://i.imgur.com/AtTcqmG.png" title="Movie Page Extra" width="100%"> |<img src="https://i.imgur.com/Eqg0bD5.png" title="Collection Page" width="100%">|<img src="https://i.imgur.com/cG22ahe.png" title="Comments" width="100%">

<h3 align="center" id="panel">Admin Panel</h3>

The structure of the admin panel was designed here for the most convenient data management, you can see the implementation in the admin.py files.

It includes pagination, searching, filtering of selected fields, specific sorting, and the ability to edit selected fields in-place.

The logic for data import/export using the [`import-export`](https://github.com/django-import-export/django-import-export) library is also implemented. For this, there is a corresponding resource for each model in the `resource.py` file.

The theme for the admin panel is based on this beautiful library - [`django-jazzmin`](https://github.com/farridav/django-jazzmin). This is how it looks:

Login Page         |  Dashboard
:-------------------------:|:-------------------------:
<img src="https://i.imgur.com/1z8z2dK.png" title="Login Page" width="100%"> |<img src="https://i.imgur.com/ahrKTRc.png" title="Dashboard" width="100%">

Model View        |  Edit View
:-------------------------:|:-------------------------:
<img src="https://i.imgur.com/7KXn3mP.png" title="Model View" width="100%"> |<img src="https://i.imgur.com/SZYIEG1.png" title="Edit View" width="100%">

<h3 align="center" id="authentication">Authentication</h3>

Authentication is used here with [`allauth`](https://django-allauth.readthedocs.io/en/latest/).

Also, confirmation of your mail is configured here through an email with a verification link, which will be sent to the specified mail, valid for 1 day.

Since Google removed access for less secure applications, the whole process related to emails is now handled by [`SendGrid`](https://sendgrid.com/), so that's why you can see the following configuration for email in the settings:

```py
EMAIL_HOST = "smtp.sendgrid.net"
```

You can see an example of registration on the site below:

Sign Up Page         |  Validation Email | Confirmation Page
:-------------------------:|:-------------------------:|:-------------------------:
<img src="https://i.imgur.com/PJyVC1L.png" title="Sign Up Page" width="100%"> |<img src="https://i.imgur.com/QNsSbId.png" title="Validation Email" width="100%">|<img src="https://i.imgur.com/GyySFnO.png" title="Confirmation Page" width="100%">

Password Reset Page         |  Password Reset Email   |  Login Page
:-------------------------:|:-------------------------:|:-------------------------:
<img src="https://i.imgur.com/TLQkUAr.png" title="Password Reset Page" width="100%"> |<img src="https://i.imgur.com/JISZ04P.png" title="Password Reset Email" width="100%">|<img src="https://i.imgur.com/TLQkUAr.png" title="Login Page" width="100%">

<h3 align="center" id="caching">Caching</h3>

At first, I wrote myself the logic for caching and resetting the cache when the state of the model object changes, but later I just gave the cache handling to this wonderful library - [`django-cacheops`](https://github.com/Suor/django-cacheops).

Now the project has caching of almost all queries, caches selected views, and in the future I think I will add caching of template fragments. Caching is never enough!

I have Redis on the server to store the cache.

<h3 align="center" id="dockerization">Dockerization</h3>

The app is fully dockerized. In the `docker` folder, you can find Dockerfiles for configuring the database (`Postgres 15.1`) and for configuring the project itself (`Python 3.11`).

Also in this folder there are bash scripts, one of which is an entrypoint for the application, and the other is used to transfer the dump of the production database to docker Postgres.

See `docker-compose.yml` for main logic.

<h3 align="center" id="debug">Debug Toolbar</h3>

For local testing (running through dev setup) debug toolbar is used, this great library is [`django-debug-toolbar`](https://github.com/jazzband/django-debug-toolbar).

These panels helped me find a bunch of problems that I later solved. Do not pass this treasure)

In the photo you can see which panels are used in this application:

Debug Toolbar View|
|:-------------------------:|
<img src="https://i.imgur.com/WOiAqBK.png" title="Debug Toolbar" width="100%"> |

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

<h2 align="center" id="platformms">🎞️ Supported Platforms</h2>

<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tbody>
    <tr>
      <td align="center"><img src="https://i.imgur.com/WK0oYMk.png" width="100px;" alt="Netflix"/><b>Netflix</b></br> 🌍🇺🇦</td>
      <td align="center"><img src="https://i.imgur.com/NPjfGty.jpg" width="100px;" alt="Megogo"/><b>Megogo</b></br> 🇺🇦</td>
      <td align="center"><img src="https://i.imgur.com/jksIrz9.png" width="100px;" alt="Kyivstar"/><b>Kyivstar TV</b></br> 🇺🇦</td>
      <td align="center"><img src="https://i.imgur.com/vUTl1sb.png" width="100px;" alt="Disney"/><b>Disney+</b></br> 🇺🇸</td>
     <td align="center"><img src="https://i.imgur.com/H2qsguX.jpg" width="100px;" alt="YouTube"/><b>YouTube TV</b> </br> 🌍</td>
     <td align="center"><img src="https://i.imgur.com/6RUEt5f.jpg" width="100px;" alt="UAkino"/><b>UAkino</b></br> 🇺🇦</td>
    </tr>
    <tr>
      <td align="center"><img src="https://i.imgur.com/qvORJK2.jpg" width="100px;" alt="HBO"/><b>HBO MAX</b></br> 🇺🇸</td>
      <td align="center"><img src="https://i.imgur.com/3vNDLk7.png" width="100px;" alt="Prime"/><b>Amazon Prime</b></br> 🇺🇸</td>
      <td align="center"><img src="https://i.imgur.com/RSorKKr.png" width="100px;" alt="AppleTV"/><b>AppleTV+</b></br> 🌍</td>
      <td align="center"><img src="https://i.imgur.com/HUxl4Lu.jpg" width="100px;" alt="Hulu"/><b>Hulu</b></br> 🇺🇸</td>
     <td align="center"><img src="https://i.imgur.com/uq2Nzg5.png" width="100px;" alt="Megogo"/><b>Peacock</b></br> 🇺🇸</td>
     <td align="center"><img src="https://i.imgur.com/Dh6SzkT.png" width="100px;" alt="Megogo"/><b>iTunes</b></br> 🌍</td>
    </tr>
    <tr>
       <td align="center"><img src="https://i.imgur.com/vPU66Cx.png" width="100px;" alt="Amazon"/><b>Amazon</b></br> 🇺🇸</td>
      <td align="center"><img src="https://i.imgur.com/ldE4BT0.jpg" width="100px;" alt="Google Play"/><b>Google Play</b></br> 🇺🇸</td>
      <td align="center"><img src="https://i.imgur.com/dSnfumV.png" width="100px;" alt="Microsoft Store"/><b>Microsoft Store</b></br> 🌍</td>
      <td align="center"><img src="https://i.imgur.com/rlkMn8N.png" width="100px;" alt="Paramount"/><b>Paramount+</b></br> 🇺🇸</td>
     <td align="center"><img src="https://i.imgur.com/Hx9zV6M.png" width="100px;" alt="Shudder"/><b>Shudder</b></br> 🇺🇸</td>
     <td align="center"><img src="https://i.imgur.com/SjxI4Lp.jpg" width="100px;" alt="Syfy"/><b>Syfy</b></br> 🇺🇸</td>
    </tr>

  </tbody>
</table>

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->


![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

<h2 align="center" id="stack">📚 Stack</h2>

- <img width=3% src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/1869px-Python-logo-notext.svg.png"> <b><a href="https://www.python.org/downloads/release/python-3110/">&nbsp;Python</a></b>
- <img width=3% src="https://cdn.worldvectorlogo.com/logos/django.svg"> <b><a href="https://docs.djangoproject.com/en/4.1/releases/4.1/">&nbsp;Django</a></b>
- <img width=3% src="https://www.django-rest-framework.org/img/logo.png"> <b><a href="https://www.django-rest-framework.org/">&nbsp;Django REST</a></b>
- <img width=3% src="https://avatars.githubusercontent.com/u/110818415?s=280&v=4g"> <b><a href="https://pydantic-docs.helpmanual.io/">&nbsp;Pydantic</a></b>
- <img width=3% src="https://upload.wikimedia.org/wikipedia/commons/a/ab/Swagger-logo.png"> <b><a href="https://drf-spectacular.readthedocs.io/en/latest/">&nbsp;Swagger</a></b>
- <img width=3% src="https://www.freeiconspng.com/thumbs/no-image-icon/no-image-icon-6.png"> <b><a href="https://github.com/Suor/django-cacheops">&nbsp;Django Cacheops  </a></b>
- <img width=3% src="https://www.freeiconspng.com/thumbs/no-image-icon/no-image-icon-6.png"> <b><a href="https://django-allauth.readthedocs.io/en/latest/">&nbsp;Django AllAuth</a></b>
- <img width=3% src="https://www.freeiconspng.com/thumbs/no-image-icon/no-image-icon-6.png"> <b><a href="https://django-jazzmin.readthedocs.io/">&nbsp;Django Jazzmin</a></b>
- <img width=3% src="https://www.freeiconspng.com/thumbs/no-image-icon/no-image-icon-6.png"> <b><a href="https://django-mptt.readthedocs.io/en/latest/">&nbsp;Django MPTT </a></b>
- <img width=3% src="https://www.freeiconspng.com/thumbs/no-image-icon/no-image-icon-6.png"> <b><a href="https://django-debug-toolbar.readthedocs.io/en/latest/">&nbsp;Django Debug Toolbar</a></b>
- <img width=3% src="https://www.freeiconspng.com/thumbs/no-image-icon/no-image-icon-6.png"> <b><a href="https://django-import-export.readthedocs.io/en/latest/">&nbsp;Django import / export</a></b>
- <img width=3% src="https://www.freeiconspng.com/thumbs/no-image-icon/no-image-icon-6.png"> <b><a href="https://django-filter.readthedocs.io/en/stable/">&nbsp;django-filter</a></b>


- <img width=3% src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/99/Unofficial_JavaScript_logo_2.svg/1024px-Unofficial_JavaScript_logo_2.svg.png"> <b><a href="https://devdocs.io/javascript/">&nbsp;JavaScript</a></b>
- <img width=3% src="https://upload.wikimedia.org/wikipedia/commons/thumb/d/d5/CSS3_logo_and_wordmark.svg/1200px-CSS3_logo_and_wordmark.svg.png"> <b><a href="https://developer.mozilla.org/en-US/docs/Web/CSS">&nbsp;CSS</a></b>
- <img width=3% src="https://cdn.iconscout.com/icon/free/png-256/jquery-10-1175155.png"> <b><a href="https://jquery.com/">&nbsp;jQuery</a></b>
- <img width=3% src="https://upload.wikimedia.org/wikipedia/commons/thumb/b/b2/Bootstrap_logo.svg/1280px-Bootstrap_logo.svg.png"> <b><a href="https://getbootstrap.com/">&nbsp;Bootstrap</a></b>


- <img width=3% src="https://www.svgrepo.com/show/331370/docker.svg"> <b><a href="https://docs.docker.com/language/python/build-images/">&nbsp;Docker</a></b>
- <img width=3% src="https://avatars.githubusercontent.com/u/44036562?s=280&v=4"> <b><a href="https://github.com/features/actions">&nbsp;GitHub Actions</a></b>
- <img width=3% src="https://pre-commit.com/logo.svg"> <b><a href="https://pre-commit.com/">&nbsp;Pre-Commit</a></b>
- <img width=3% src="https://upload.wikimedia.org/wikipedia/commons/thumb/2/29/Postgresql_elephant.svg/993px-Postgresql_elephant.svg.png"> <b><a href="">&nbsp;PostgreSQL</a></b>
- <img width=3% src="https://w7.pngwing.com/pngs/70/860/png-transparent-redis-distributed-cache-database-caching-chess24-angle-logo-data-thumbnail.png"> <b><a href="">&nbsp;Redis</a></b>
- <img width=3% src="https://cdn.worldvectorlogo.com/logos/gunicorn.svg"> <b><a href="https://gunicorn.org/">Gunicorn</a></b>


![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

<h2 align="center" id="contributors">✨ Contributors</h2>


<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table align="center">
  <tr>
   <td align="center"><a href="https://github.com/Russkiy-Voyennyy-Korabl-Idi-Nakhuy"><img src="https://avatars.githubusercontent.com/u/43554620??v=4?s=200" width="200px;" alt="Jack Shendrikov"/><br/><sub><b>👑 Jack Shendrikov 👑</b></sub></a></td>
  </tr>
</table>

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

<div align="center">✨ 🍰 ✨</div>
