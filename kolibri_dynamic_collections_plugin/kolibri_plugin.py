from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals

from kolibri.core.content import hooks as content_hooks
from kolibri.core.hooks import NavigationHook
from kolibri.core.webpack import hooks as webpack_hooks
from kolibri.plugins import KolibriPluginBase
from kolibri.plugins.hooks import register_hook
from le_utils.constants import format_presets


class DynamicCollectionsPlugin(KolibriPluginBase):
    translated_view_urls = "urls"


@register_hook
class DynamicCollectionsNavItem(NavigationHook):
    bundle_id = "side_nav"


@register_hook
class DynamicCollectionsAsset(webpack_hooks.WebpackBundleHook):
    bundle_id = "app"

    @property
    def plugin_data(self):
        return {}
