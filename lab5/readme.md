## Lab 5

Welcome! This week we will continue working with the database, and we will add visualization methods.

## Before you get started

Perform the steps A1-10 listed in the [labs.md](../lab0/labs.md) file as usual.

If you have run out of apps on heroku, you may delete your lab1 or lab3 apps from the heroku dashboard.

## Modifying the database

This time, we won't be creating a *new* database, we'll be re-using your last one.

1. Copy your `.env` file from lab4 into the lab5 directory.

2. CRUD (Create - Read - Update - Delete) operations
    + A brief introduction to managing database entries through your routes:
        + Two functionalities are pre-build - check out the `/user/create/[...]` and `user/read/<uid>` routes in app.py.
        + You will need to fix the following routes to expand your ability to interact with the database: `/user/read_all`, `user/update/[...]`, `/user/delete/<uid>`.
        + You will also need to rewire users.css to handle listing multiple users using Jinja2.
        
3. Test your app in flask, and then publish to heroku and retest there.

## Visualization (If we have time)

1. Let's finish up our histogram by adding some styling and labels.
    + On the way let's consider d3's `join` method:
        + An enter / update / exit pattern exists (analogous to adding / modifying / removing elements from the DOM).
        + A simple build-in alternative: pass a single element (in this case a `'rect'`) directly.
        
2. Some tips for getting started on the donut and scatterplot charts:
    + Make use of [Observable](https://observablehq.com/) for examples on how to build charts.
    + Start with the scatterplot - the approach and code is very similar to what we've covered in 'bars'.
    + The donut chart is a bit more challenging, and you should take time to look at two tools offered by d3: `group` and `pie`.
    
## Homework

1. Add new form templates to:
    + Add new users using your `/user/create/[...]` route.
    + Modify users using your `/user/update/[...]` route.
    
2. Modify the `list.html` template with a button which opens the form for creating new users.

3. Modify the user table on the `list.html` template with links to the forms you created in step 1 to allow users to modify/delete users using your new CRUD methods.

4. Complete the `donut.js` chart where indicated, using the examples given in class.

5. Complete the `scatter.js` chart where indicated, using the examples given in class and previous steps above.

6. EXTRA: When hovering over a bar, donut segment, or scatterplot dot in any of the charts: 
    + Change the color to indicate it is being selected.
    + Reveal a popup which shows the underlying numerical value.
    + When the hover is complete (the mouse leaves the element) the element should revert to its previous state.

