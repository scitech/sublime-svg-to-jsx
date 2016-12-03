# Convert SVG to JSX
This plugin replaces SVG attributes with their JSX-valid equivalents and deletes common JSX-invalid attribute strings.

## When is this useful?
- If you're working on a React project with a lot of manual SVG manipulation.
- If you're tired of repetitive find + replacing on the SVG assets pasted from Sketch or Illustrator.

## Example
Say you have some SVG output from your graphics editor that you'd like to include in a React component. Using the markup directly will raise errors:
```jsx
function Box() {
  return (
    <svg width="115px" height="125px" viewBox="0 0 115 125" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
      <rect id="Rectangle" stroke="none" fill="#D8D8D8" fill-rule="evenodd" x="0" y="0" width="115" height="125"></rect>
    </svg>
  )
}
```

This plugin, accessible from the right-click menu and the main menu, will remove invalid properties and correct the casing of valid properties so you can use the SVG in a component's render method without errors:
```jsx
function Box() {
  return (
    <svg width="115px" height="125px" viewBox="0 0 115 125" version="1.1">
      <rect id="Rectangle" stroke="none" fill="#D8D8D8" fillRule="evenodd" x="0" y="0" width="115" height="125"></rect>
    </svg>
  )
}
```

For complex illustrations with several distinct components to be animated, this can be quite useful!

## When is this not useful?
- If you want to automatically load SVG files to use directly as React components. Try https://github.com/jhamlet/svg-react-loader.
