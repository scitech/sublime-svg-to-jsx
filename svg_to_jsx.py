import sublime
import sublime_plugin

REPLACEMENTS = [
    ('accent-height', 'accentHeight'),
    ('alignment-baseline', 'alignmentBaseline'),
    ('arabic-form', 'arabicForm'),
    ('baseline-shift', 'baselineShift'),
    ('cap-height', 'capHeight'),
    ('clip-path', 'clipPath'),
    ('clip-rule', 'clipRule'),
    ('color-interpolation', 'colorInterpolation'),
    ('color-interpolation-filters', 'colorInterpolationFilters'),
    ('color-profile', 'colorProfile'),
    ('color-rendering', 'colorRendering'),
    ('dominant-baseline', 'dominantBaseline'),
    ('enable-background', 'enableBackground'),
    ('fill-opacity', 'fillOpacity'),
    ('fill-rule', 'fillRule'),
    ('flood-color', 'floodColor'),
    ('flood-opacity', 'floodOpacity'),
    ('font-family', 'fontFamily'),
    ('font-size', 'fontSize'),
    ('font-size-adjust', 'fontSizeAdjust'),
    ('font-stretch', 'fontStretch'),
    ('font-style', 'fontStyle'),
    ('font-variant', 'fontVariant'),
    ('font-weight', 'fontWeight'),
    ('glyph-name', 'glyphName'),
    ('glyph-orientation-horizontal', 'glyphOrientationHorizontal'),
    ('glyph-orientation-vertical', 'glyphOrientationVertical'),
    ('horiz-adv-x', 'horizAdvX'),
    ('horiz-origin-x', 'horizOriginX'),
    ('image-rendering', 'imageRendering'),
    ('letter-spacing', 'letterSpacing'),
    ('lighting-color', 'lightingColor'),
    ('marker-end', 'markerEnd'),
    ('marker-mid', 'markerMid'),
    ('marker-start', 'markerStart'),
    ('overline-position', 'overlinePosition'),
    ('overline-thickness', 'overlineThickness'),
    ('panose-1', 'panose1'),
    ('paint-order', 'paintOrder'),
    ('rendering-intent', 'renderingIntent'),
    ('shape-rendering', 'shapeRendering'),
    ('stop-color', 'stopColor'),
    ('stop-opacity', 'stopOpacity'),
    ('strikethrough-position', 'strikethroughPosition'),
    ('strikethrough-thickness', 'strikethroughThickness'),
    ('stroke-dasharray', 'strokeDasharray'),
    ('stroke-dashoffset', 'strokeDashoffset'),
    ('stroke-linecap', 'strokeLinecap'),
    ('stroke-linejoin', 'strokeLinejoin'),
    ('stroke-miterlimit', 'strokeMiterlimit'),
    ('stroke-opacity', 'strokeOpacity'),
    ('stroke-width', 'strokeWidth'),
    ('text-anchor', 'textAnchor'),
    ('text-decoration', 'textDecoration'),
    ('text-rendering', 'textRendering'),
    ('underline-position', 'underlinePosition'),
    ('underline-thickness', 'underlineThickness'),
    ('unicode-bidi', 'unicodeBidi'),
    ('unicode-range', 'unicodeRange'),
    ('units-per-em', 'unitsPerEm'),
    ('v-alphabetic', 'vAlphabetic'),
    ('v-hanging', 'vHanging'),
    ('v-ideographic', 'vIdeographic'),
    ('v-mathematical', 'vMathematical'),
    ('vert-adv-y', 'vertAdvY'),
    ('vert-origin-x', 'vertOriginX'),
    ('vert-origin-y', 'vertOriginY'),
    ('word-spacing', 'wordSpacing'),
    ('writing-mode', 'writingMode'),
    ('x-height', 'xHeight'),
    ('xlink:actuate', 'xlinkActuate'),
    ('xlink:arcrole', 'xlinkArcrole'),
    ('xlink:href', 'xlinkHref'),
    ('xlink:role', 'xlinkRole'),
    ('xlink:show', 'xlinkShow'),
    ('xlink:title', 'xlinkTitle'),
    ('xlink:type', 'xlinkType'),
    ('xml:base', 'xmlBase'),
    ('xml:lang', 'xmlLang'),
    ('xml:space', 'xmlSpace')
]

DELETIONS = [
    'xmlns:xlink=".*?"',
    'xmlns=".*?"',
    'line-spacing=".*?"'
]

class ConvertSvgToJsxCommand(sublime_plugin.TextCommand):
    """Convert SVG in the open buffer to valid JSX."""
    def run(self, edit):
        for target in DELETIONS:
            self.erase_all(edit, target)

        for attr in REPLACEMENTS:
            # replace all with this attribute
            self.replace_all(edit, attr[0], attr[1])


    def replace_all(self, edit, target, replacement):
        """Replace all occurences of a pattern."""
        regions = self.view.find_all(target)

        # Perform the replacement in reverse to avoid offsetting issues
        for region in reversed(regions):
            self.view.replace(edit, region, replacement)


    def erase_all(self, edit, target):
        """Erase all occurences of a pattern."""
        regions = self.view.find_all(target)

        # Perform the deletion in reverse to avoid offsetting issues
        for region in reversed(regions):
            self.view.erase(edit, region)
