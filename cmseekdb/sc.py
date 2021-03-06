#!/usr/bin/python3
# -*- coding: utf-8 -*-
# This is a part of CMSeeK, check the LICENSE file for more information
# Copyright (c) 2018 Tuhinshubhra

# This file contains all the methods of detecting cms via Source Code
# Version: 1.0.0
# Return a list with ['1'/'0','ID of CMS'/'na'] 1 = detected 0 = not detected 2 = No Sourcecode Provided

import re

def check(s, site): ## Check if no generator meta tag available
    if s == "": ## No source code provided kinda shitty check but oh well
        return ['2', 'na']
    else: ## The real shit begins here
        hstring = s
        # harray = s.split("\n") ### Array conversion can use if needed later
        if '/wp-content/' in hstring:
            # WordPress
            return ['1','wp']

        elif '/skin/frontend/' in hstring:
            # Magento
            return ['1','mg']

        elif 'https://www.blogger.com/static/' in hstring:
            # Blogger By Google
            return ['1','blg']

        elif 'ic.pics.livejournal.com' in hstring:
            # LiveJournal
            return ['1','lj']

        elif 'END: 3dcart stats' in hstring:
            # 3D Cart
            return ['1','tdc']

        elif 'href="/apos-minified/' in hstring:
            # Apostrophe CMS
            return ['1','apos']

        # elif 'WebFontConfig = ' in hstring:
        #    # Bubble CMS
        #    return ['1','bubble']

        elif 'href="/CatalystStyles/' in hstring:
            # Adobe Business Catalyst
            return ['1','abc']

        elif 'src="/misc/drupal.js"' in hstring:
            # Drupal
            return ['1', 'dru']

        elif 'css/joomla.css' in hstring: # Lamest one possible
             # Obvious Joomla
             return ['1','joom']

        elif 'Powered By <a href="http://www.opencart.com">OpenCart' in hstring or "catalog/view/javascript/jquery/swiper/css/opencart.css" in hstring or 'index.php?route=' in hstring:
            # OpenCart
            return ['1', 'oc']

        elif '/xoops.js' in hstring or 'xoops_redirect' in hstring:
            # XOOPS
            return ['1', 'xoops']

        elif 'Wolf Default RSS Feed' in hstring:
            # Wolf CMS
            return ['1', 'wolf']

        elif '/ushahidi.js' in hstring or 'alt="Ushahidi"' in hstring:
            # ushahidi (weird freaking name)
            return ['1', 'ushahidi']

        elif 'getWebguiProperty' in hstring:
            # WebGUI
            return ['1', 'wgui']

        elif 'title: "TiddlyWiki"' in hstring or 'TiddlyWiki created by Jeremy Ruston,' in hstring:
            # Tiddly Wiki
            return ['1','tidw']

        elif 'Running Squiz Matrix' in hstring:
            # Squiz Matrix
            return ['1', 'sqm']

        elif 'assets.spin-cdn.com' in hstring:
            # Spin CMS
            return ['1', 'spin']

        elif 'content="Solodev" name="author"' in hstring:
            # solodev
            return ['1', 'sdev']

        elif 'content="sNews' in hstring:
            # sNews
            return ['1', 'snews']

        elif '/api/sitecore/' in hstring:
            # sitecore
            return ['1', 'score']

        elif 'simsite/' in hstring:
            # SIMsite
            return ['1', 'sim']

        elif 'simplebo.net/' in hstring  or '"pswp__' in hstring:
            # Simplebo
            return ['1', 'spb']

        elif '/silvatheme' in hstring:
            # Silva CMS
            return ['1', 'silva']

        elif 'serendipityQuickSearchTermField' in hstring  or '"serendipity_' in hstring or 'serendipity[' in hstring:
            # Serendipity
            return ['1', 'spity']

        elif 'Published by Seamless.CMS.WebUI' in hstring:
            # SeamlessCMS
            return ['1', 'slcms']

        elif 'rock-config-trigger' in hstring or 'rock-config-cancel-trigger' in hstring:
            # RockRMS
            return ['1', 'rock']

        elif '/rcms-f-production.' in hstring:
            # RCMS
            return ['1', 'rcms']

        elif 'CMS by Quick.Cms' in hstring or 'read license: www.opensolution.org/license.html' in hstring:
            # Quick.Cms
            return ['1', 'quick']

        elif '"pimcore_' in hstring:
            # Pimcore
            return ['1', 'pcore']

        elif 'xmlns:perc' in hstring or 'cm/css/perc_decoration.css' in hstring:
            # Percussion CMS
            return ['1', 'percms']

        elif 'PencilBlueController' in hstring or '"pencilblueApp"' in hstring:
            # PencilBlue
            return ['1', 'pblue']

        elif '/libraries/ophal.js' in hstring:
            # Ophal
            return ['1', 'ophal']

        elif 'Sitefinity/WebsiteTemplates' in hstring:
            # Sitefinity
            return ['1', 'sfy']

        elif 'published by Open Text Web Solutions' in hstring:
            # OpenText WSM
            return ['1', 'otwsm']

        elif '/opencms/export/' in hstring:
            # OpenCms
            return ['1', 'ocms']

        elif 'odoo.session_info' in hstring or 'var odoo =' in hstring:
            # Odoo
            return ['1', 'odoo']

        elif '_spBodyOnLoadWrapper' in hstring or '_spPageContextInfo' in hstring or '_spFormOnSubmitWrapper' in hstring:
            # Microsoft SharePoint
            return ['1', 'share']

        elif '/storage/app/media/' in hstring:
            # October CMS
            return ['1', 'octcms']

        elif 'mura.min.css' in hstring or '/plugins/Mura' in hstring:
            # Mura CMS
            return ['1', 'mura']

        elif 'mt-content/' in hstring or 'moto-website-style' in hstring:
            # Moto CMS
            return ['1', 'moto']

        elif 'mono_donottrack' in hstring or 'monotracker.js' in hstring  or '_monoTracker' in hstring:
            # Mono.net
            return ['1', 'mnet']

        elif 'Powered by MODX</a>' in hstring:
            # MODX
            return ['1', 'modx']

        elif "siteCMS:'methode'" in hstring or "contentOriginatingCMS='Methode'" in hstring or 'Methode tags version' in hstring or '/r/PortalConfig/common/assets/' in hstring:
            # Methode
            return ['1', 'methd']

        elif 'var LIVESTREET_SECURITY_KEY' in hstring:
            # LiveStreet CMS
            return ['1', 'lscms']

        elif '/koken.js' in hstring or 'data-koken-internal' in hstring:
            # Koken
            return ['1', 'koken']

        elif 'jimdo_layout_css' in hstring or 'var jimdoData' in hstring or 'isJimdoMobileApp' in hstring:
            # Jimdo
            return ['1', 'jimdo']

        elif '<!-- you must provide a link to Indexhibit' in hstring or "Built with <a href='http://www.indexhibit.org/'>Indexhibit" in hstring or 'ndxz-studio/site' in hstring or 'ndxzsite/' in hstring:
            # IndexHibit
            return ['1', 'ibit']

        elif '<!-- webflow css -->' in hstring or 'css/webflow.css' in hstring or 'js/webflow.js' in hstring:
            # Webflow CMS
            return ['1', 'wflow']

        elif 'css/jalios/core/' in hstring or 'js/jalios/core/' in hstring or 'jalios:ready' in hstring:
            # jalios JCMS
            return ['1', 'jcms']

        elif 'ip_themes/' in hstring or 'ip_libs/' in hstring or 'ip_cms/' in hstring:
            # ImpressPages CMS
            return ['1', 'impage']

        elif '/css_js_cache/hotaru_css' in hstring or 'hotaruFooterImg' in hstring or '/css_js_cache/hotaru_js' in hstring:
            # Hotaru CMS
            return ['1', 'hotaru']

        elif 'binaries/content/gallery/' in hstring:
            # Hippo CMS
            return ['1', 'hippo']

        elif 'PHP-Nuke Copyright ©' in hstring or 'PHP-Nuke theme by' in hstring:
            # PHP Nuke
            return ['1', 'phpn']

        elif 'FlexCMP - CMS per Siti Accessibili' in hstring or '/flex/TemplatesUSR/' in hstring or 'FlexCMP - Digital Experience Platform (DXP)' in hstring:
            # FlexCMP
            return ['1', 'flex']

        elif 'copyright" content="eZ Systems"' in hstring or 'ezcontentnavigationpart' in hstring or 'ezinfo/copyright' in hstring:
            # eZ Publish
            return ['1', 'ezpu']

        elif 'e107_files/e107.js' in hstring or 'e107_themes/' in hstring or 'e107_plugins/' in hstring:
            # e107
            return ['1', 'e107']

        elif '<!-- DNN Platform' in hstring or ' by DNN Corporation -->' in hstring or 'DNNROBOTS' in hstring or 'js/dnncore.js?' in hstring or 'dnn_ContentPane' in hstring or 'js/dnn.js?' in hstring:
            # DNN Platform
            return['1', 'dnn']

        elif 'phpBBstyle' in hstring or 'phpBBMobileStyle' in hstring or 'style_cookie_settings' in hstring:
            # phpBB
            return ['1', 'phpbb']

        elif 'dede_fields' in hstring or 'dede_fieldshash' in hstring or 'DedeAjax' in hstring or 'DedeXHTTP' in hstring or 'include/dedeajax2.js' in hstring or 'css/dedecms.css' in hstring:
            # DEDE CMS
            return ['1', 'dede']

        elif '/Orchard.jQuery/' in hstring or 'orchard.themes' in hstring or 'orchard-layouts-root' in hstring:
            # Orchard CMS
            return ['1', 'orchd']

        elif 'modules/contentbox/themes/' in hstring:
            # ContentBox
            return ['1', 'cbox']

        elif 'data-contentful' in hstring or '.contentful.com/' in hstring or '.ctfassets.net/' in hstring:
            # Contentful
            return ['1', 'conful']

        elif 'Contensis.current' in hstring or 'ContensisSubmitFromTextbox' in hstring or 'ContensisTextOnly' in hstring:
            # Contensis
            return ['1', 'contensis']

        elif 'system/cron/cron.txt' in hstring:
            # Contao
            return ['1', 'contao']

        elif '/concrete/images' in hstring or '/concrete/css' in hstring or '/concrete/js' in hstring:
            # Concrete5 CMS
            return ['1', 'con5']

        hippo_regex = re.search(r'binaries/(.*?)/content/gallery/', hstring)
        if hippo_regex != None:
            # Hippo CMS
            return ['1', 'hippo']

        phpc_regex = re.search(r'.php\?m=(.*?)&c=(.*?)&a=(.*?)&catid=', hstring)
        if phpc_regex != None:
            # phpCMS
            return ['1', 'phpc']

        pb_regex = re.search(r'Powered by (.*?)phpBB', hstring)
        if pb_regex != None:
            # phpBB
            return ['1', 'phpbb']

        pb_regex = re.search(r'copyright(.*?)phpBB Group', hstring)
        if pb_regex != None:
            # phpBB
            return ['1', 'phpbb']

        coton_regex = re.search(r'Powered by(.*?)Cotonti', hstring)
        if coton_regex != None:
            # Cotonti
            return ['1', 'coton']

        con_regex = re.search(r'CCM_(.*?)(_|)(MODE|URL|PATH|FILENAME|REL|CID)', hstring)
        if con_regex != None:
            # Concrete5 CMS
            return ['1', 'con5']

        else:
            # Failure
            return ['0', 'na']
