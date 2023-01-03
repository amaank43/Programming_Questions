<!-- https://devsnest.in/frontend-challenges/javascript/js-script-tag/132-->

<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <title>Mocha Tests</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  </head>
  <body>
    <!-- Add a script tag with id internal and a script tag with id external -->
    <!-- internal script tag should be empty without linking any external script file -->
    <!-- external script tag should contain an src attribute that links index.js -->
    <!-- note: index.js already exists in the same folder you just have to link it with the help of using a script tag with id external -->

    <!-- code from here -->
    <script id='internal'></script>
    <script id='external' src='index.js'></script>
    <!-- to here -->

  <!-- Don't remove this mocha file -->
  <div id="mocha"></div>
  <script type="module" src="./src/setup.js"></script>
  <script type="module" src="./src/run.js"></script>
</body>

</html>
