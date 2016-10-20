import sublime
import sublime_plugin

REPLACEMENTS = [
    ('stroke-width', 'strokeWidth'),
    ('stroke-linecap', 'strokeLinecap'),
    ('stroke-linejoin', 'strokeLinejoin'),
    ('fill-rule', 'fillRule'),
    ('xlink:href', 'xlinkHref')
]

DELETIONS = [
    'xmlns:xlink="http://www.w3.org/1999/xlink"',
    'xmlns="http://www.w3.org/2000/svg"'
]

class ConvertCommand(sublime_plugin.TextCommand):
    """Convert SVG in the open buffer to valid JSX."""
    def run(self, edit):
        regions = []

        for target in DELETIONS:
            self.erase_all(edit, target)

        for attr in REPLACEMENTS:
            # replace all with this attribute
            self.replace_all(edit, attr[0], attr[1])


    def replace_all(self, edit, target, replacement):
        """Replace all occurences of a pattern."""
        regions = self.view.find_all(target)
        difference = len(replacement) - len(target)

        # Make sure regions are accurate when replacing multiple
        offset_regions = []
        for index, region in enumerate(regions):
            offset_regions.append(sublime.Region(region.begin() + (difference * index), region.end() + (difference * index)))

        # Perform the replacement
        for region in offset_regions:
            self.view.replace(edit, region, replacement)


    def erase_all(self, edit, target):
        """Erase all occurences of a pattern."""
        regions = self.view.find_all(target)
        offset_length = len(target)

        # Make sure regions are accurate when erasing multiple
        offset_regions = []
        for index, region in enumerate(regions):
            offset_regions.append(
                sublime.Region(region.begin() - (offset_length * index), region.end() - (offset_length * index))
            )

        # Perform the deletion
        for region in offset_regions:
            print(region)
            self.view.erase(edit, region)
