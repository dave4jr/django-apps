#*====================== #
#*  Author:		 Dave Luke Jr
#*  Company:	 CenterStack.io
#*  Description:	 aura/urls.py
#*====================== #

from django.conf.urls import patterns, url, include

# ==================================================#
#	URL Conf
# ==================================================#
urlpatterns = patterns('',
	url(r'^404/$', 'aura.views.navigation', {"template":"404.html"}, name="aura-404"),
	url(r'^404/$', 'aura.views.navigation', {"template":"404.html"}, name="aura-404"),
	url(r'^500/$', 'aura.views.navigation', {"template":"500.html"}, name="aura-500"),
	url(r'^about-about-1/$', 'aura.views.navigation', {"template":"about-about-1.html"}, name="aura-about-about-1"),
	url(r'^about-about-2/$', 'aura.views.navigation', {"template":"about-about-2.html"}, name="aura-about-about-2"),
	url(r'^about-about-3/$', 'aura.views.navigation', {"template":"about-about-3.html"}, name="aura-about-about-3"),
	url(r'^about-about-4/$', 'aura.views.navigation', {"template":"about-about-4.html"}, name="aura-about-about-4"),
	url(r'^accordions/$', 'aura.views.navigation', {"template":"accordions.html"}, name="aura-accordions"),
	url(r'^alert-boxes/$', 'aura.views.navigation', {"template":"alert-boxes.html"}, name="aura-alert-boxes"),
	url(r'^animations/$', 'aura.views.navigation', {"template":"animations.html"}, name="aura-animations"),
	url(r'^blog-blog-grid-sidebar/$', 'aura.views.navigation', {"template":"blog-blog-grid-sidebar.html"}, name="aura-blog-blog-grid-sidebar"),
	url(r'^blog-blog-grid-wide/$', 'aura.views.navigation', {"template":"blog-blog-grid-wide.html"}, name="aura-blog-blog-grid-wide"),
	url(r'^blog-blog-large-image/$', 'aura.views.navigation', {"template":"blog-blog-large-image.html"}, name="aura-blog-blog-large-image"),
	url(r'^blog-blog-medium-image/$', 'aura.views.navigation', {"template":"blog-blog-medium-image.html"}, name="aura-blog-blog-medium-image"),
	url(r'^blog-blog-single-post/$', 'aura.views.navigation', {"template":"blog-blog-single-post.html"}, name="aura-blog-blog-single-post"),
	url(r'^blog-blog-small-image/$', 'aura.views.navigation', {"template":"blog-blog-small-image.html"}, name="aura-blog-blog-small-image"),
	url(r'^blog-blog-timeline-sidebar/$', 'aura.views.navigation', {"template":"blog-blog-timeline-sidebar.html"}, name="aura-blog-blog-timeline-sidebar"),
	url(r'^blog-blog-timeline-wide/$', 'aura.views.navigation', {"template":"blog-blog-timeline-wide.html"}, name="aura-blog-blog-timeline-wide"),
	url(r'^boxes/$', 'aura.views.navigation', {"template":"boxes.html"}, name="aura-boxes"),
	url(r'^buttons/$', 'aura.views.navigation', {"template":"buttons.html"}, name="aura-buttons"),
	url(r'^clients-clients-1/$', 'aura.views.navigation', {"template":"clients-clients-1.html"}, name="aura-clients-clients-1"),
	url(r'^clients-clients-2/$', 'aura.views.navigation', {"template":"clients-clients-2.html"}, name="aura-clients-clients-2"),
	url(r'^clients-clients-3/$', 'aura.views.navigation', {"template":"clients-clients-3.html"}, name="aura-clients-clients-3"),
	url(r'^clients-clients-4/$', 'aura.views.navigation', {"template":"clients-clients-4.html"}, name="aura-clients-clients-4"),
	url(r'^clients-clients-5/$', 'aura.views.navigation', {"template":"clients-clients-5.html"}, name="aura-clients-clients-5"),
	url(r'^clients-clients-6/$', 'aura.views.navigation', {"template":"clients-clients-6.html"}, name="aura-clients-clients-6"),
	url(r'^clients-clients-7/$', 'aura.views.navigation', {"template":"clients-clients-7.html"}, name="aura-clients-clients-7"),
	url(r'^contact-contact-1-fancy-header/$', 'aura.views.navigation', {"template":"contact-contact-1-fancy-header.html"}, name="aura-contact-contact-1-fancy-header"),
	url(r'^contact-contact-2-fancy-header/$', 'aura.views.navigation', {"template":"contact-contact-2-fancy-header.html"}, name="aura-contact-contact-2-fancy-header"),
	url(r'^counters-numbers/$', 'aura.views.navigation', {"template":"counters-numbers.html"}, name="aura-counters-numbers"),
	url(r'^counters-progress-bars/$', 'aura.views.navigation', {"template":"counters-progress-bars.html"}, name="aura-counters-progress-bars"),
	url(r'^docs-accordions/$', 'aura.views.navigation', {"template":"docs-accordions.html"}, name="aura-docs-accordions"),
	url(r'^docs-alert-boxes/$', 'aura.views.navigation', {"template":"docs-alert-boxes.html"}, name="aura-docs-alert-boxes"),
	url(r'^docs-boxes/$', 'aura.views.navigation', {"template":"docs-boxes.html"}, name="aura-docs-boxes"),
	url(r'^docs-captcha/$', 'aura.views.navigation', {"template":"docs-captcha.html"}, name="aura-docs-captcha"),
	url(r'^docs-changelog/$', 'aura.views.navigation', {"template":"docs-changelog.html"}, name="aura-docs-changelog"),
	url(r'^docs-colorbox/$', 'aura.views.navigation', {"template":"docs-colorbox.html"}, name="aura-docs-colorbox"),
	url(r'^docs-credits/$', 'aura.views.navigation', {"template":"docs-credits.html"}, name="aura-docs-credits"),
	url(r'^docs-docs/$', 'aura.views.navigation', {"template":"docs-docs.html"}, name="aura-docs-docs"),
	url(r'^docs-dropcaps/$', 'aura.views.navigation', {"template":"docs-dropcaps.html"}, name="aura-docs-dropcaps"),
	url(r'^docs-galleries/$', 'aura.views.navigation', {"template":"docs-galleries.html"}, name="aura-docs-galleries"),
	url(r'^docs-global-helpers/$', 'aura.views.navigation', {"template":"docs-global-helpers.html"}, name="aura-docs-global-helpers"),
	url(r'^docs-google-maps/$', 'aura.views.navigation', {"template":"docs-google-maps.html"}, name="aura-docs-google-maps"),
	url(r'^docs-grid/$', 'aura.views.navigation', {"template":"docs-grid.html"}, name="aura-docs-grid"),
	url(r'^docs-header/$', 'aura.views.navigation', {"template":"docs-header.html"}, name="aura-docs-header"),
	url(r'^docs-icon-boxes/$', 'aura.views.navigation', {"template":"docs-icon-boxes.html"}, name="aura-docs-icon-boxes"),
	url(r'^docs-icons/$', 'aura.views.navigation', {"template":"docs-icons.html"}, name="aura-docs-icons"),
	url(r'^docs-lists/$', 'aura.views.navigation', {"template":"docs-lists.html"}, name="aura-docs-lists"),
	url(r'^docs-quick-start-guide/$', 'aura.views.navigation', {"template":"docs-quick-start-guide.html"}, name="aura-docs-quick-start-guide"),
	url(r'^docs-responsive-helpers/$', 'aura.views.navigation', {"template":"docs-responsive-helpers.html"}, name="aura-docs-responsive-helpers"),
	url(r'^docs-sections/$', 'aura.views.navigation', {"template":"docs-sections.html"}, name="aura-docs-sections"),
	url(r'^docs-slider/$', 'aura.views.navigation', {"template":"docs-slider.html"}, name="aura-docs-slider"),
	url(r'^docs-socials/$', 'aura.views.navigation', {"template":"docs-socials.html"}, name="aura-docs-socials"),
	url(r'^docs-subscribe-forms/$', 'aura.views.navigation', {"template":"docs-subscribe-forms.html"}, name="aura-docs-subscribe-forms"),
	url(r'^docs-tables/$', 'aura.views.navigation', {"template":"docs-tables.html"}, name="aura-docs-tables"),
	url(r'^docs-tabs/$', 'aura.views.navigation', {"template":"docs-tabs.html"}, name="aura-docs-tabs"),
	url(r'^docs-theme-settings/$', 'aura.views.navigation', {"template":"docs-theme-settings.html"}, name="aura-docs-theme-settings"),
	url(r'^docs-theme-structure/$', 'aura.views.navigation', {"template":"docs-theme-structure.html"}, name="aura-docs-theme-structure"),
	url(r'^docs-titlebars-breadcrumbs/$', 'aura.views.navigation', {"template":"docs-titlebars-breadcrumbs.html"}, name="aura-docs-titlebars-breadcrumbs"),
	url(r'^docs-twitter-feed/$', 'aura.views.navigation', {"template":"docs-twitter-feed.html"}, name="aura-docs-twitter-feed"),
	url(r'^faq-faq-1/$', 'aura.views.navigation', {"template":"faq-faq-1.html"}, name="aura-faq-faq-1"),
	url(r'^faq-faq-2/$', 'aura.views.navigation', {"template":"faq-faq-2.html"}, name="aura-faq-faq-2"),
	url(r'^footers-footers-base/$', 'aura.views.navigation', {"template":"footers-footers-base.html"}, name="aura-footers-footers-base"),
	url(r'^footers-footers-dark/$', 'aura.views.navigation', {"template":"footers-footers-dark.html"}, name="aura-footers-footers-dark"),
	url(r'^footers-footers-light/$', 'aura.views.navigation', {"template":"footers-footers-light.html"}, name="aura-footers-footers-light"),
	url(r'^forms/$', 'aura.views.navigation', {"template":"forms.html"}, name="aura-forms"),
	url(r'^google-maps-dark/$', 'aura.views.navigation', {"template":"google-maps-dark.html"}, name="aura-google-maps-dark"),
	url(r'^google-maps-grey/$', 'aura.views.navigation', {"template":"google-maps-grey.html"}, name="aura-google-maps-grey"),
	url(r'^google-maps-hybrid/$', 'aura.views.navigation', {"template":"google-maps-hybrid.html"}, name="aura-google-maps-hybrid"),
	url(r'^google-maps-roadmap/$', 'aura.views.navigation', {"template":"google-maps-roadmap.html"}, name="aura-google-maps-roadmap"),
	url(r'^google-maps-satellite/$', 'aura.views.navigation', {"template":"google-maps-satellite.html"}, name="aura-google-maps-satellite"),
	url(r'^headers-headers-base/$', 'aura.views.navigation', {"template":"headers-headers-base.html"}, name="aura-headers-headers-base"),
	url(r'^headers-headers-dark/$', 'aura.views.navigation', {"template":"headers-headers-dark.html"}, name="aura-headers-headers-dark"),
	url(r'^headers-headers-light/$', 'aura.views.navigation', {"template":"headers-headers-light.html"}, name="aura-headers-headers-light"),
	url(r'^home-home-10/$', 'aura.views.navigation', {"template":"home-home-10.html"}, name="aura-home-home-10"),
	url(r'^home-home-11/$', 'aura.views.navigation', {"template":"home-home-11.html"}, name="aura-home-home-11"),
	url(r'^home-home-12/$', 'aura.views.navigation', {"template":"home-home-12.html"}, name="aura-home-home-12"),
	url(r'^home-home-1/$', 'aura.views.navigation', {"template":"home-home-1.html"}, name="aura-home-home-1"),
	url(r'^home-home-2/$', 'aura.views.navigation', {"template":"home-home-2.html"}, name="aura-home-home-2"),
	url(r'^home-home-3/$', 'aura.views.navigation', {"template":"home-home-3.html"}, name="aura-home-home-3"),
	url(r'^home-home-4/$', 'aura.views.navigation', {"template":"home-home-4.html"}, name="aura-home-home-4"),
	url(r'^home-home-5/$', 'aura.views.navigation', {"template":"home-home-5.html"}, name="aura-home-home-5"),
	url(r'^home-home-6/$', 'aura.views.navigation', {"template":"home-home-6.html"}, name="aura-home-home-6"),
	url(r'^home-home-7/$', 'aura.views.navigation', {"template":"home-home-7.html"}, name="aura-home-home-7"),
	url(r'^home-home-8/$', 'aura.views.navigation', {"template":"home-home-8.html"}, name="aura-home-home-8"),
	url(r'^home-home-9/$', 'aura.views.navigation', {"template":"home-home-9.html"}, name="aura-home-home-9"),
	url(r'^home-onepage-1/$', 'aura.views.navigation', {"template":"home-onepage-1.html"}, name="aura-home-onepage-1"),
	url(r'^home-onepage-2/$', 'aura.views.navigation', {"template":"home-onepage-2.html"}, name="aura-home-onepage-2"),
	url(r'^home-onepage-3/$', 'aura.views.navigation', {"template":"home-onepage-3.html"}, name="aura-home-onepage-3"),
	url(r'^icon-boxes-horizontal/$', 'aura.views.navigation', {"template":"icon-boxes-horizontal.html"}, name="aura-icon-boxes-horizontal"),
	url(r'^icon-boxes-vertical/$', 'aura.views.navigation', {"template":"icon-boxes-vertical.html"}, name="aura-icon-boxes-vertical"),
	url(r'^icons/$', 'aura.views.navigation', {"template":"icons.html"}, name="aura-icons"),
	url(r'^images/$', 'aura.views.navigation', {"template":"images.html"}, name="aura-images"),
	url(r'^index/$', 'aura.views.navigation', {"template":"index.html"}, name="aura-index"),
	url(r'^layouts-fixed-fluid-fixed/$', 'aura.views.navigation', {"template":"layouts-fixed-fluid-fixed.html"}, name="aura-layouts-fixed-fluid-fixed"),
	url(r'^layouts-fixed-fluid/$', 'aura.views.navigation', {"template":"layouts-fixed-fluid.html"}, name="aura-layouts-fixed-fluid"),
	url(r'^layouts-fluid-fixed/$', 'aura.views.navigation', {"template":"layouts-fluid-fixed.html"}, name="aura-layouts-fluid-fixed"),
	url(r'^lists-groups/$', 'aura.views.navigation', {"template":"lists-groups.html"}, name="aura-lists-groups"),
	url(r'^lists-icons/$', 'aura.views.navigation', {"template":"lists-icons.html"}, name="aura-lists-icons"),
	url(r'^lists-images/$', 'aura.views.navigation', {"template":"lists-images.html"}, name="aura-lists-images"),
	url(r'^lists-simple/$', 'aura.views.navigation', {"template":"lists-simple.html"}, name="aura-lists-simple"),
	url(r'^modals/$', 'aura.views.navigation', {"template":"modals.html"}, name="aura-modals"),
	url(r'^portfolio-portfolio-1/$', 'aura.views.navigation', {"template":"portfolio-portfolio-1.html"}, name="aura-portfolio-portfolio-1"),
	url(r'^portfolio-portfolio-10/$', 'aura.views.navigation', {"template":"portfolio-portfolio-10.html"}, name="aura-portfolio-portfolio-10"),
	url(r'^portfolio-portfolio-2/$', 'aura.views.navigation', {"template":"portfolio-portfolio-2.html"}, name="aura-portfolio-portfolio-2"),
	url(r'^portfolio-portfolio-3/$', 'aura.views.navigation', {"template":"portfolio-portfolio-3.html"}, name="aura-portfolio-portfolio-3"),
	url(r'^portfolio-portfolio-4/$', 'aura.views.navigation', {"template":"portfolio-portfolio-4.html"}, name="aura-portfolio-portfolio-4"),
	url(r'^portfolio-portfolio-5/$', 'aura.views.navigation', {"template":"portfolio-portfolio-5.html"}, name="aura-portfolio-portfolio-5"),
	url(r'^portfolio-portfolio-6/$', 'aura.views.navigation', {"template":"portfolio-portfolio-6.html"}, name="aura-portfolio-portfolio-6"),
	url(r'^portfolio-portfolio-7/$', 'aura.views.navigation', {"template":"portfolio-portfolio-7.html"}, name="aura-portfolio-portfolio-7"),
	url(r'^portfolio-portfolio-8/$', 'aura.views.navigation', {"template":"portfolio-portfolio-8.html"}, name="aura-portfolio-portfolio-8"),
	url(r'^portfolio-portfolio-9/$', 'aura.views.navigation', {"template":"portfolio-portfolio-9.html"}, name="aura-portfolio-portfolio-9"),
	url(r'^portfolio-portfolio-masonry-2/$', 'aura.views.navigation', {"template":"portfolio-portfolio-masonry-2.html"}, name="aura-portfolio-portfolio-masonry-2"),
	url(r'^portfolio-portfolio-masonry/$', 'aura.views.navigation', {"template":"portfolio-portfolio-masonry.html"}, name="aura-portfolio-portfolio-masonry"),
	url(r'^portfolio-portfolio-single/$', 'aura.views.navigation', {"template":"portfolio-portfolio-single.html"}, name="aura-portfolio-portfolio-single"),
	url(r'^portfolio-portfolio-timeline/$', 'aura.views.navigation', {"template":"portfolio-portfolio-timeline.html"}, name="aura-portfolio-portfolio-timeline"),
	url(r'^pricing-tables/$', 'aura.views.navigation', {"template":"pricing-tables.html"}, name="aura-pricing-tables"),
	url(r'^sections/$', 'aura.views.navigation', {"template":"sections.html"}, name="aura-sections"),
	url(r'^services-services-1/$', 'aura.views.navigation', {"template":"services-services-1.html"}, name="aura-services-services-1"),
	url(r'^services-services-10/$', 'aura.views.navigation', {"template":"services-services-10.html"}, name="aura-services-services-10"),
	url(r'^services-services-11/$', 'aura.views.navigation', {"template":"services-services-11.html"}, name="aura-services-services-11"),
	url(r'^services-services-2/$', 'aura.views.navigation', {"template":"services-services-2.html"}, name="aura-services-services-2"),
	url(r'^services-services-3/$', 'aura.views.navigation', {"template":"services-services-3.html"}, name="aura-services-services-3"),
	url(r'^services-services-4/$', 'aura.views.navigation', {"template":"services-services-4.html"}, name="aura-services-services-4"),
	url(r'^services-services-5/$', 'aura.views.navigation', {"template":"services-services-5.html"}, name="aura-services-services-5"),
	url(r'^services-services-6/$', 'aura.views.navigation', {"template":"services-services-6.html"}, name="aura-services-services-6"),
	url(r'^services-services-7/$', 'aura.views.navigation', {"template":"services-services-7.html"}, name="aura-services-services-7"),
	url(r'^services-services-8/$', 'aura.views.navigation', {"template":"services-services-8.html"}, name="aura-services-services-8"),
	url(r'^services-services-9/$', 'aura.views.navigation', {"template":"services-services-9.html"}, name="aura-services-services-9"),
	url(r'^sign-in/$', 'aura.views.navigation', {"template":"sign-in.html"}, name="aura-sign-in"),
	url(r'^sign-up/$', 'aura.views.navigation', {"template":"sign-up.html"}, name="aura-sign-up"),
	url(r'^slider/$', 'aura.views.navigation', {"template":"slider.html"}, name="aura-slider"),
	url(r'^socials-big/$', 'aura.views.navigation', {"template":"socials-big.html"}, name="aura-socials-big"),
	url(r'^socials-simple/$', 'aura.views.navigation', {"template":"socials-simple.html"}, name="aura-socials-simple"),
	url(r'^socials-small/$', 'aura.views.navigation', {"template":"socials-small.html"}, name="aura-socials-small"),
	url(r'^socials/$', 'aura.views.navigation', {"template":"socials.html"}, name="aura-socials"),
	url(r'^tables/$', 'aura.views.navigation', {"template":"tables.html"}, name="aura-tables"),
	url(r'^tabs-big/$', 'aura.views.navigation', {"template":"tabs-big.html"}, name="aura-tabs-big"),
	url(r'^tabs/$', 'aura.views.navigation', {"template":"tabs.html"}, name="aura-tabs"),
	url(r'^team-team-1/$', 'aura.views.navigation', {"template":"team-team-1.html"}, name="aura-team-team-1"),
	url(r'^team-team-2/$', 'aura.views.navigation', {"template":"team-team-2.html"}, name="aura-team-team-2"),
	url(r'^team-team-3/$', 'aura.views.navigation', {"template":"team-team-3.html"}, name="aura-team-team-3"),
	url(r'^testimonials-photo/$', 'aura.views.navigation', {"template":"testimonials-photo.html"}, name="aura-testimonials-photo"),
	url(r'^testimonials-simple/$', 'aura.views.navigation', {"template":"testimonials-simple.html"}, name="aura-testimonials-simple"),
	url(r'^testimonials-testimonials-1/$', 'aura.views.navigation', {"template":"testimonials-testimonials-1.html"}, name="aura-testimonials-testimonials-1"),
	url(r'^testimonials-testimonials-2/$', 'aura.views.navigation', {"template":"testimonials-testimonials-2.html"}, name="aura-testimonials-testimonials-2"),
	url(r'^titlebars-big-breadcrumb-right/$', 'aura.views.navigation', {"template":"titlebars-big-breadcrumb-right.html"}, name="aura-titlebars-big-breadcrumb-right"),
	url(r'^titlebars-big-breadcrumb-top/$', 'aura.views.navigation', {"template":"titlebars-big-breadcrumb-top.html"}, name="aura-titlebars-big-breadcrumb-top"),
	url(r'^titlebars-only-breadcrumb/$', 'aura.views.navigation', {"template":"titlebars-only-breadcrumb.html"}, name="aura-titlebars-only-breadcrumb"),
	url(r'^titlebars-small-breadcrumb-right/$', 'aura.views.navigation', {"template":"titlebars-small-breadcrumb-right.html"}, name="aura-titlebars-small-breadcrumb-right"),
	url(r'^titlebars-small-breadcrumb-top/$', 'aura.views.navigation', {"template":"titlebars-small-breadcrumb-top.html"}, name="aura-titlebars-small-breadcrumb-top"),
	url(r'^typo/$', 'aura.views.navigation', {"template":"typo.html"}, name="aura-typo"),
	url(r'^utility-utility-alignment/$', 'aura.views.navigation', {"template":"utility-utility-alignment.html"}, name="aura-utility-utility-alignment"),
	url(r'^utility-utility-grid/$', 'aura.views.navigation', {"template":"utility-utility-grid.html"}, name="aura-utility-utility-grid"),
	url(r'^utility-utility-visibility/$', 'aura.views.navigation', {"template":"utility-utility-visibility.html"}, name="aura-utility-utility-visibility")
)