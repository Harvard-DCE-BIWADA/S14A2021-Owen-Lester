# Lab 3.5 Bootstrap Tutorial

Welcome! In this tutorial, we'll be demonstrating a way to incorporate the Bootstrap framework into your web projects.

_Note: While we're using Bootstrap for this tutorial, the principles we describe here can be applied to any responsive CSS/Javascript framework into your websites._

## Before We Begin...

There are a few concepts and documents we'll wish to familiarize ourselves with before we get started:

### Links

1. [Mozilla Developer Network](https://developer.mozilla.org/en-US/docs/Web) - An excellent repository of reference information for CSS, Javascript and Web development generally.
2. [Bootstrap](https://getbootstrap.com) - The main Bootstrap website, containing API documentation, reference and examples.
3. [Jinja Project](https://jinja.palletsprojects.com/en/2.11.x/) - The Jinja Project website, which contains information on the Jinja templating language we'll be using in the lab.

### Glossary of Terms
Let's go over a couple of terms that we'll use in the following tutorial. You should familiarize yourselves with these terms, as they will be used frequently throughout the material and documentation, and it is important for you to know what they are, as well as how and _why_ they are used.

[**CSS**](https://developer.mozilla.org/en-US/docs/Web/CSS)  - Cascading Style Sheets is a markup language used to define the _presentation_, or "style" of a document, such as an Webpage, HTML or XML file. The _Cascading_ qualifier means that as new styles are added, the web browser or rendering engine will apply new new styles on top of the previously defined styles, allowing you to customize styles with a minimum of effort. The current version of CSS is CSS3, which is what we will be using in this courses moving forward.

CSS rules can be added to separate files:
```
<!doctype html>

<html lang="en">
<head>
    <meta charset="utf-8">

    <title>My Super-Awesome S14A Project</title>
    <meta name="viewport" content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <meta name="description" content="My Super-Awesome S14A Project">
    <meta name="author" content="The Like, Coolest Person EVER">

    <link rel="stylesheet" href="static/css/base.css?v=1.0">
    <link rel="stylesheet" href="static/css/custom.css?v=1.0">
</head>

<body>
    <p class="my-class">Hello!</p>
    <script src="static/js/scripts.js"></script>
</body>
</html>
```

```
// \file static/css/base.css
.my-class {
    color: red;
    border-width: 1 px;
}
```
```
// \file static/css/custom.css
.my-class {
    color: blue;
}
```

Directly in HTML:

```
<!doctype html>

<html lang="en">
<head>
    <meta charset="utf-8">

    <title>My Super-Awesome S14A Project</title>
    <meta name="viewport" content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <meta name="description" content="My Super-Awesome S14A Project">
    <meta name="author" content="The Like, Coolest Person EVER">

    <link rel="stylesheet" href="static/css/base.css?v=1.0">
    <style>
        .my-class { color: blue; }
    </style>
</head>

<body>
    <p class="my-class">Hello!</p>
    <script src="static/js/scripts.js"></script>
</body>
</html>
```

Or may be defined directly when marking up specific elements:

```
<!doctype html>

<html lang="en">
<head>
<head>
    <meta charset="utf-8">

    <title>My Super-Awesome S14A Project</title>
    <meta name="viewport" content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <meta name="description" content="My Super-Awesome S14A Project">
    <meta name="author" content="The Like, Coolest Person EVER">

    <link rel="stylesheet" href="static/css/base.css?v=1.0">
</head>

<body>
    <p class="my-class" style="color: blue;">Hello!</p>
    <script src="static/js/scripts.js"></script>
</body>
</html>
```
It is important to remember that CSS rules are applied **in the order seen by the browser**. A list of the CSS properties that can be modified can be found [here](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference).

[**CSS Box Model**](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Box_Model/Introduction_to_the_CSS_box_model) - The _CSS Box Model_ defines all elements of a webpage as inhabiting a "box" (really a nested set of boxen) containing the actual _content_ to be displayed, _padding_ around the content, an optional _border_ surrounding the padded area, and finally a _margin_ which surrounds the border, controlling the spacing between other elements on the page.

![CSS Box Model](https://mdn.mozillademos.org/files/8685/boxmodel-(3).png)
    Image Source: https://mdn.mozillademos.org/files/8685/boxmodel-(3).png

Each of these components of an individual "box" can be controlled by an appropriate CSS rule.

[**DOM**](https://developer.mozilla.org/en-US/docs/Web/API/Document_Object_Model) - The _Document Object Model_ is an abstraction API which describes all components of a website (and even the browser itself) into a set of objects or "elements" which have both _properties_ and _operations_. The properties which dictate how these elements are displayed on screen are controlled by the defined CSS rules. These CSS rules are selectively applied to elements based on _selectors_, such as element _name_, _class_, or _id_. DOM elements are also the primary means through which Javascript interacts with a webpage and the elements it contains.

[**Template (Language)**](https://en.wikipedia.org/wiki/Web_template_system) - A Templating language (such as Jinja) allows for code/markup reuse by defining the basic structure of a webpage or document, leaving placeholders for programmers to customize the _content_. This is also known as the "separation of concerns" allowing a programmer to focus on the design and structure, and someone else to focus on the content. Placeholders for the custom content are usually implemented using _keywords_ or _tags_, and may facilitate the usage of _control structures_ such as _loops_ or _if statements_ to minimize the amount of code that needs to be written. Templates are usually _composable_, meaning they can include other templates inside of them, allowing for extensive customization. 


```
<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">

    <title>My Super-Awesome S14A Project</title>
    <meta name="viewport" content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <meta name="description" content="My Super-Awesome S14A Project">
    <meta name="author" content="The Like, Coolest Person EVER">

    <!-- Styles -->
    <link href="{{ url_for('static', filename='./css/base.css') }}" rel="stylesheet">
    {% block styles %}
    {% endblock %}

</head>
<body>

    <!-- Content -->
    {% block content %}
    {% endblock %}


    <!-- Scripts -->
    {% block scripts %}
    {% endblock %}
</body>
</html>
```

[**Responsive Design**](https://developer.mozilla.org/en-US/docs/Learn/CSS/CSS_layout/Responsive_Design) - The _Responsive Design_ paradigm is development practice for ensuring that webpages are rendered effectively regardless of device characteristics such as _screen resolution_, _window size_, _device type_ or _orientation_.

![Responsive Design Example](https://www.w3schools.com/css/img_temp_band.jpg)
    Image Source: https://www.w3schools.com/css/img_temp_band.jpg

## Bootstrap
Before we begin, let's head over to the Bootstrap website, and explore a little bit: [https://getbootstrap.com](https://getbootstrap.com)

Like most frameworks, the site contains rich documentation, and many examples that programmers such as yourselves can use to create rich and responsive websites.

There are two main ways to add Bootstrap (or other Frameworks) to your site:

1. CDN (Content Delivery Network)
2. Static Embedding

**Question**: Who knows the strengths and weaknesses of each method? Can you think three pros/cons for each method?

In this  tutorial, we're going to use the Static Embedding method because it is easier to view the framework code this way.

1. Download the ___Compiled JS and CSS___ from the Bootstrap downloads page: https://getbootstrap.com/docs/4.5/getting-started/download/
    + Unzip the files
    + Copy the _contents_ of the `<download_location>/<bootstraap_folder>/css/` directory into your project's `static/css/` directory.
    + Copy the _contents_ of the `<download_location>/<bootstraap_folder>/js/` directory into your project's `static/js/` directory.
    
2. Link the Bootstrap stylesheet into your project by modifying your projects `templates/layout.html` file:
    + Replace the line containing
          
          `<link href="{{ url_for('static', filename='./css/reset.css') }}" rel="stylesheet">`
      with
          
          `<link href="{{ url_for('static', filename='./css/bootstrap.css') }}" rel="stylesheet">`
    
3. Link the Bootstrap Javascript files into your project by modifying your projects `templates/layout.html` file:
    + Paste the following code on a new line after the `<!-- Scripts -->` line:
        `<script src="{{ url_for('static', filename='./js/bootstrap.js') }}" ></script>`
    
    + **Question**: Why are we including these files in the `layout.html` file? What would happen if we placed them in other places?
    
4. For Bootstrap to function properly, we'll also need to add jQuery and Popper to the mix. Let's do that using the CDN method:
    + Paste the following code ***before*** the Bootstrap line added in step 3:
    
        `<script src="https://code.jquery.com/jquery-3.5.1.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>`
        
        `<script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.1/dist/umd/popper.min.js" integrity="sha384-9/reFTGAW83EW2RDu2S0VKaIzap3H66lZH81PoYlFhbGU+6BZp6G7niu735Sk7lN" crossorigin="anonymous"></script>`
    + **Question**: Why did we add this _before_ the bootstrap file? What would happen if we put it in afterwards?
    
5. Ensure your Python/Conda environment are _active_, and run your Flask app as shown in previous tutorials:

    `conda activate <env>`
    
    `flask run`
    
    + **Question**: Some immediate changes should be noticed, why is that?
    
6. Head over to the Bootstrap form example: https://getbootstrap.com/docs/4.0/examples/checkout/
    + Inspect the code using your browser's "Code Inspector"
    
7. Open your project's `form.html` file.
    + Comment out the line containing
        `<link href="{{ url_for('static', filename='./css/form.css') }}" rel="stylesheet">`
        
        by adding `{#` and `#}` as comment tags:
        
        `{#<link href="{{ url_for('static', filename='./css/form.css') }}" rel="stylesheet"> #}`

        + **Question**: Why did we comment these out?
        
    + Add the following to the `<form>` tag:
        + under `class="form"`, add the `needs-validation` class
        + at the end, add `novalidate`
        
        `<form class="form needs-validation" method="POST" action="/predict" novalidate>`
    
        + **Question**: Why did we add these two lines?
        
    + Modify the `{{ field }}` tag to add the required class information:
        
        `{{ field(class="form-control") }}`
        
    + Modify the `{{form.submit}}` tag to  add the required class information:
    
        `{{ form.submit(class="btn btn-primary btn-lg btn-block") }}`
        
8. We've added some tags, but if we add invalid input, we still get errors.
    
    + **Question**: Why are we seeing these?
    + Adding extra Validators is left as an exercise to the reader. This will become important later when we discuss security.
    
9. Let's add some Navigation! Head to https://getbootstrap.com/docs/4.0/examples/sticky-footer-navbar/

    + Inspect the nav bar, and copy the `<header>` code.

10. In your project's `layout.html` file:
    
    + Paste the copied HTML just below the `<body>` tag.
    + Replace the text within the `<a class="navbar-brand"..>` code with an appropriate name.
        
        `Fixed navbar` -> `My Cool Project`
        
    + Under the second Nav item, change the `href` and content appropriately:
    
        `<a clas="nav-link" href="form">Form</a>`
    
 11. Let's try it out!
 
    + Uh, oh! Where's our prediction?
    
    + **Question**: What happened to it? How would we find it?
    
    + Fix the problem by adding `<main role="main" class="container">` before the `index.html` file's `{% block content}` tag.
    + Then add `</main>` after the `{% endblock %}` tag.
    
    + Uh, oh! What's missing?
    + As an exercise, re-add the `reset.css` file with the contents of the custom css for the template.
    
12. Try doing the same thing with the footer from that same example: https://getbootstrap.com/docs/4.0/examples/sticky-footer-navbar/

  