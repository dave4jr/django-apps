#*====================== #
#*  Author:		 Dave Luke Jr
#*  Company:	 CenterStack.io
#*  Description:	 jango/urls.py
#*====================== #

from django.conf.urls import patterns, url, include

# ==================================================#
#	URL Conf
# ==================================================#
urlpatterns = patterns('',
	url(r'^breadcrumbs-bgimage-1/$', 'jango.views.navigation', {"template":"breadcrumbs-bgimage-1.html"}, name="jango-breadcrumbs-bgimage-1"),
	url(r'^breadcrumbs-bgimage-1/$', 'jango.views.navigation', {"template":"breadcrumbs-bgimage-1.html"}, name="jango-breadcrumbs-bgimage-1"),
	url(r'^breadcrumbs-bgimage-10/$', 'jango.views.navigation', {"template":"breadcrumbs-bgimage-10.html"}, name="jango-breadcrumbs-bgimage-10"),
	url(r'^breadcrumbs-bgimage-2/$', 'jango.views.navigation', {"template":"breadcrumbs-bgimage-2.html"}, name="jango-breadcrumbs-bgimage-2"),
	url(r'^breadcrumbs-bgimage-3/$', 'jango.views.navigation', {"template":"breadcrumbs-bgimage-3.html"}, name="jango-breadcrumbs-bgimage-3"),
	url(r'^breadcrumbs-bgimage-4/$', 'jango.views.navigation', {"template":"breadcrumbs-bgimage-4.html"}, name="jango-breadcrumbs-bgimage-4"),
	url(r'^breadcrumbs-bgimage-5/$', 'jango.views.navigation', {"template":"breadcrumbs-bgimage-5.html"}, name="jango-breadcrumbs-bgimage-5"),
	url(r'^breadcrumbs-bgimage-6/$', 'jango.views.navigation', {"template":"breadcrumbs-bgimage-6.html"}, name="jango-breadcrumbs-bgimage-6"),
	url(r'^breadcrumbs-bgimage-7/$', 'jango.views.navigation', {"template":"breadcrumbs-bgimage-7.html"}, name="jango-breadcrumbs-bgimage-7"),
	url(r'^breadcrumbs-bgimage-8/$', 'jango.views.navigation', {"template":"breadcrumbs-bgimage-8.html"}, name="jango-breadcrumbs-bgimage-8"),
	url(r'^breadcrumbs-bgimage-9/$', 'jango.views.navigation', {"template":"breadcrumbs-bgimage-9.html"}, name="jango-breadcrumbs-bgimage-9"),
	url(r'^breadcrumbs-default/$', 'jango.views.navigation', {"template":"breadcrumbs-default.html"}, name="jango-breadcrumbs-default"),
	url(r'^breadcrumbs-subtitle/$', 'jango.views.navigation', {"template":"breadcrumbs-subtitle.html"}, name="jango-breadcrumbs-subtitle"),
	url(r'^component-abouts/$', 'jango.views.navigation', {"template":"component-abouts.html"}, name="jango-component-abouts"),
	url(r'^component-accordions/$', 'jango.views.navigation', {"template":"component-accordions.html"}, name="jango-component-accordions"),
	url(r'^component-alerts/$', 'jango.views.navigation', {"template":"component-alerts.html"}, name="jango-component-alerts"),
	url(r'^component-app-showcase/$', 'jango.views.navigation', {"template":"component-app-showcase.html"}, name="jango-component-app-showcase"),
	url(r'^component-bars/$', 'jango.views.navigation', {"template":"component-bars.html"}, name="jango-component-bars"),
	url(r'^component-blockquotes/$', 'jango.views.navigation', {"template":"component-blockquotes.html"}, name="jango-component-blockquotes"),
	url(r'^component-blog-elements/$', 'jango.views.navigation', {"template":"component-blog-elements.html"}, name="jango-component-blog-elements"),
	url(r'^component-buttons/$', 'jango.views.navigation', {"template":"component-buttons.html"}, name="jango-component-buttons"),
	url(r'^component-clients/$', 'jango.views.navigation', {"template":"component-clients.html"}, name="jango-component-clients"),
	url(r'^component-colors/$', 'jango.views.navigation', {"template":"component-colors.html"}, name="jango-component-colors"),
	url(r'^component-counters/$', 'jango.views.navigation', {"template":"component-counters.html"}, name="jango-component-counters"),
	url(r'^component-custom-icons/$', 'jango.views.navigation', {"template":"component-custom-icons.html"}, name="jango-component-custom-icons"),
	url(r'^component-dividers/$', 'jango.views.navigation', {"template":"component-dividers.html"}, name="jango-component-dividers"),
	url(r'^component-features-2/$', 'jango.views.navigation', {"template":"component-features-2.html"}, name="jango-component-features-2"),
	url(r'^component-features/$', 'jango.views.navigation', {"template":"component-features.html"}, name="jango-component-features"),
	url(r'^component-fontawesome-icons/$', 'jango.views.navigation', {"template":"component-fontawesome-icons.html"}, name="jango-component-fontawesome-icons"),
	url(r'^component-form-controls/$', 'jango.views.navigation', {"template":"component-form-controls.html"}, name="jango-component-form-controls"),
	url(r'^component-glyphicons-icons/$', 'jango.views.navigation', {"template":"component-glyphicons-icons.html"}, name="jango-component-glyphicons-icons"),
	url(r'^component-headings/$', 'jango.views.navigation', {"template":"component-headings.html"}, name="jango-component-headings"),
	url(r'^component-labels-badges/$', 'jango.views.navigation', {"template":"component-labels-badges.html"}, name="jango-component-labels-badges"),
	url(r'^component-latest-items/$', 'jango.views.navigation', {"template":"component-latest-items.html"}, name="jango-component-latest-items"),
	url(r'^component-latest-works/$', 'jango.views.navigation', {"template":"component-latest-works.html"}, name="jango-component-latest-works"),
	url(r'^component-lists/$', 'jango.views.navigation', {"template":"component-lists.html"}, name="jango-component-lists"),
	url(r'^component-media-embeds/$', 'jango.views.navigation', {"template":"component-media-embeds.html"}, name="jango-component-media-embeds"),
	url(r'^component-modals/$', 'jango.views.navigation', {"template":"component-modals.html"}, name="jango-component-modals"),
	url(r'^component-navs/$', 'jango.views.navigation', {"template":"component-navs.html"}, name="jango-component-navs"),
	url(r'^component-paginations/$', 'jango.views.navigation', {"template":"component-paginations.html"}, name="jango-component-paginations"),
	url(r'^component-panels/$', 'jango.views.navigation', {"template":"component-panels.html"}, name="jango-component-panels"),
	url(r'^component-parallax-1/$', 'jango.views.navigation', {"template":"component-parallax-1.html"}, name="jango-component-parallax-1"),
	url(r'^component-parallax-2/$', 'jango.views.navigation', {"template":"component-parallax-2.html"}, name="jango-component-parallax-2"),
	url(r'^component-pricing-tables-1/$', 'jango.views.navigation', {"template":"component-pricing-tables-1.html"}, name="jango-component-pricing-tables-1"),
	url(r'^component-pricing-tables-2/$', 'jango.views.navigation', {"template":"component-pricing-tables-2.html"}, name="jango-component-pricing-tables-2"),
	url(r'^component-progress-bars/$', 'jango.views.navigation', {"template":"component-progress-bars.html"}, name="jango-component-progress-bars"),
	url(r'^component-services/$', 'jango.views.navigation', {"template":"component-services.html"}, name="jango-component-services"),
	url(r'^component-shop-1/$', 'jango.views.navigation', {"template":"component-shop-1.html"}, name="jango-component-shop-1"),
	url(r'^component-shop-2/$', 'jango.views.navigation', {"template":"component-shop-2.html"}, name="jango-component-shop-2"),
	url(r'^component-shop-3/$', 'jango.views.navigation', {"template":"component-shop-3.html"}, name="jango-component-shop-3"),
	url(r'^component-shop-4/$', 'jango.views.navigation', {"template":"component-shop-4.html"}, name="jango-component-shop-4"),
	url(r'^component-shop-5/$', 'jango.views.navigation', {"template":"component-shop-5.html"}, name="jango-component-shop-5"),
	url(r'^component-shop-6/$', 'jango.views.navigation', {"template":"component-shop-6.html"}, name="jango-component-shop-6"),
	url(r'^component-shop-7/$', 'jango.views.navigation', {"template":"component-shop-7.html"}, name="jango-component-shop-7"),
	url(r'^component-simpleline-icons/$', 'jango.views.navigation', {"template":"component-simpleline-icons.html"}, name="jango-component-simpleline-icons"),
	url(r'^component-social-icons/$', 'jango.views.navigation', {"template":"component-social-icons.html"}, name="jango-component-social-icons"),
	url(r'^component-steps/$', 'jango.views.navigation', {"template":"component-steps.html"}, name="jango-component-steps"),
	url(r'^component-tabbed-contents/$', 'jango.views.navigation', {"template":"component-tabbed-contents.html"}, name="jango-component-tabbed-contents"),
	url(r'^component-tables/$', 'jango.views.navigation', {"template":"component-tables.html"}, name="jango-component-tables"),
	url(r'^component-tabs/$', 'jango.views.navigation', {"template":"component-tabs.html"}, name="jango-component-tabs"),
	url(r'^component-team/$', 'jango.views.navigation', {"template":"component-team.html"}, name="jango-component-team"),
	url(r'^component-testimonials-2/$', 'jango.views.navigation', {"template":"component-testimonials-2.html"}, name="jango-component-testimonials-2"),
	url(r'^component-testimonials/$', 'jango.views.navigation', {"template":"component-testimonials.html"}, name="jango-component-testimonials"),
	url(r'^component-tiles/$', 'jango.views.navigation', {"template":"component-tiles.html"}, name="jango-component-tiles"),
	url(r'^footer-1/$', 'jango.views.navigation', {"template":"footer-1.html"}, name="jango-footer-1"),
	url(r'^footer-2/$', 'jango.views.navigation', {"template":"footer-2.html"}, name="jango-footer-2"),
	url(r'^footer-3/$', 'jango.views.navigation', {"template":"footer-3.html"}, name="jango-footer-3"),
	url(r'^footer-4/$', 'jango.views.navigation', {"template":"footer-4.html"}, name="jango-footer-4"),
	url(r'^footer-5/$', 'jango.views.navigation', {"template":"footer-5.html"}, name="jango-footer-5"),
	url(r'^footer-6/$', 'jango.views.navigation', {"template":"footer-6.html"}, name="jango-footer-6"),
	url(r'^footer-7/$', 'jango.views.navigation', {"template":"footer-7.html"}, name="jango-footer-7"),
	url(r'^footer-8/$', 'jango.views.navigation', {"template":"footer-8.html"}, name="jango-footer-8"),
	url(r'^footer-9/$', 'jango.views.navigation', {"template":"footer-9.html"}, name="jango-footer-9"),
	url(r'^home-10/$', 'jango.views.navigation', {"template":"home-10.html"}, name="jango-home-10"),
	url(r'^home-11/$', 'jango.views.navigation', {"template":"home-11.html"}, name="jango-home-11"),
	url(r'^home-12/$', 'jango.views.navigation', {"template":"home-12.html"}, name="jango-home-12"),
	url(r'^home-2/$', 'jango.views.navigation', {"template":"home-2.html"}, name="jango-home-2"),
	url(r'^home-3/$', 'jango.views.navigation', {"template":"home-3.html"}, name="jango-home-3"),
	url(r'^home-4/$', 'jango.views.navigation', {"template":"home-4.html"}, name="jango-home-4"),
	url(r'^home-5/$', 'jango.views.navigation', {"template":"home-5.html"}, name="jango-home-5"),
	url(r'^home-6/$', 'jango.views.navigation', {"template":"home-6.html"}, name="jango-home-6"),
	url(r'^home-7/$', 'jango.views.navigation', {"template":"home-7.html"}, name="jango-home-7"),
	url(r'^home-8/$', 'jango.views.navigation', {"template":"home-8.html"}, name="jango-home-8"),
	url(r'^home-9/$', 'jango.views.navigation', {"template":"home-9.html"}, name="jango-home-9"),
	url(r'^home-header-1-ext/$', 'jango.views.navigation', {"template":"home-header-1-ext.html"}, name="jango-home-header-1-ext"),
	url(r'^home-header-1/$', 'jango.views.navigation', {"template":"home-header-1.html"}, name="jango-home-header-1"),
	url(r'^home-header-2-ext/$', 'jango.views.navigation', {"template":"home-header-2-ext.html"}, name="jango-home-header-2-ext"),
	url(r'^home-header-2/$', 'jango.views.navigation', {"template":"home-header-2.html"}, name="jango-home-header-2"),
	url(r'^home-header-3/$', 'jango.views.navigation', {"template":"home-header-3.html"}, name="jango-home-header-3"),
	url(r'^home-header-4-ext/$', 'jango.views.navigation', {"template":"home-header-4-ext.html"}, name="jango-home-header-4-ext"),
	url(r'^home-header-4/$', 'jango.views.navigation', {"template":"home-header-4.html"}, name="jango-home-header-4"),
	url(r'^home-header-5-ext/$', 'jango.views.navigation', {"template":"home-header-5-ext.html"}, name="jango-home-header-5-ext"),
	url(r'^home-header-5/$', 'jango.views.navigation', {"template":"home-header-5.html"}, name="jango-home-header-5"),
	url(r'^home-header-6-ext/$', 'jango.views.navigation', {"template":"home-header-6-ext.html"}, name="jango-home-header-6-ext"),
	url(r'^home-header-6/$', 'jango.views.navigation', {"template":"home-header-6.html"}, name="jango-home-header-6"),
	url(r'^home-header-7/$', 'jango.views.navigation', {"template":"home-header-7.html"}, name="jango-home-header-7"),
	url(r'^home-header-8/$', 'jango.views.navigation', {"template":"home-header-8.html"}, name="jango-home-header-8"),
	url(r'^index/$', 'jango.views.navigation', {"template":"index.html"}, name="jango-index"),
	url(r'^inner-header-1-ext/$', 'jango.views.navigation', {"template":"inner-header-1-ext.html"}, name="jango-inner-header-1-ext"),
	url(r'^inner-header-1/$', 'jango.views.navigation', {"template":"inner-header-1.html"}, name="jango-inner-header-1"),
	url(r'^inner-header-2-ext/$', 'jango.views.navigation', {"template":"inner-header-2-ext.html"}, name="jango-inner-header-2-ext"),
	url(r'^inner-header-2/$', 'jango.views.navigation', {"template":"inner-header-2.html"}, name="jango-inner-header-2"),
	url(r'^inner-header-3/$', 'jango.views.navigation', {"template":"inner-header-3.html"}, name="jango-inner-header-3"),
	url(r'^inner-header-4/$', 'jango.views.navigation', {"template":"inner-header-4.html"}, name="jango-inner-header-4"),
	url(r'^inner-header-5/$', 'jango.views.navigation', {"template":"inner-header-5.html"}, name="jango-inner-header-5"),
	url(r'^megamenu-dark/$', 'jango.views.navigation', {"template":"megamenu-dark.html"}, name="jango-megamenu-dark"),
	url(r'^megamenu-light/$', 'jango.views.navigation', {"template":"megamenu-light.html"}, name="jango-megamenu-light"),
	url(r'^onepage-1/$', 'jango.views.navigation', {"template":"onepage-1.html"}, name="jango-onepage-1"),
	url(r'^onepage-10/$', 'jango.views.navigation', {"template":"onepage-10.html"}, name="jango-onepage-10"),
	url(r'^onepage-11/$', 'jango.views.navigation', {"template":"onepage-11.html"}, name="jango-onepage-11"),
	url(r'^onepage-12/$', 'jango.views.navigation', {"template":"onepage-12.html"}, name="jango-onepage-12"),
	url(r'^onepage-2/$', 'jango.views.navigation', {"template":"onepage-2.html"}, name="jango-onepage-2"),
	url(r'^onepage-3/$', 'jango.views.navigation', {"template":"onepage-3.html"}, name="jango-onepage-3"),
	url(r'^onepage-4/$', 'jango.views.navigation', {"template":"onepage-4.html"}, name="jango-onepage-4"),
	url(r'^onepage-5/$', 'jango.views.navigation', {"template":"onepage-5.html"}, name="jango-onepage-5"),
	url(r'^onepage-6/$', 'jango.views.navigation', {"template":"onepage-6.html"}, name="jango-onepage-6"),
	url(r'^onepage-7/$', 'jango.views.navigation', {"template":"onepage-7.html"}, name="jango-onepage-7"),
	url(r'^onepage-8/$', 'jango.views.navigation', {"template":"onepage-8.html"}, name="jango-onepage-8"),
	url(r'^onepage-9/$', 'jango.views.navigation', {"template":"onepage-9.html"}, name="jango-onepage-9"),
	url(r'^page-2col-portfolio/$', 'jango.views.navigation', {"template":"page-2col-portfolio.html"}, name="jango-page-2col-portfolio"),
	url(r'^page-4col-portfolio/$', 'jango.views.navigation', {"template":"page-4col-portfolio.html"}, name="jango-page-4col-portfolio"),
	url(r'^page-about-1/$', 'jango.views.navigation', {"template":"page-about-1.html"}, name="jango-page-about-1"),
	url(r'^page-about-2/$', 'jango.views.navigation', {"template":"page-about-2.html"}, name="jango-page-about-2"),
	url(r'^page-about-3/$', 'jango.views.navigation', {"template":"page-about-3.html"}, name="jango-page-about-3"),
	url(r'^page-about-4/$', 'jango.views.navigation', {"template":"page-about-4.html"}, name="jango-page-about-4"),
	url(r'^page-blog-grid/$', 'jango.views.navigation', {"template":"page-blog-grid.html"}, name="jango-page-blog-grid"),
	url(r'^page-blog-list/$', 'jango.views.navigation', {"template":"page-blog-list.html"}, name="jango-page-blog-list"),
	url(r'^page-blog-post/$', 'jango.views.navigation', {"template":"page-blog-post.html"}, name="jango-page-blog-post"),
	url(r'^page-contact-1/$', 'jango.views.navigation', {"template":"page-contact-1.html"}, name="jango-page-contact-1"),
	url(r'^page-contact-2/$', 'jango.views.navigation', {"template":"page-contact-2.html"}, name="jango-page-contact-2"),
	url(r'^page-contact-3/$', 'jango.views.navigation', {"template":"page-contact-3.html"}, name="jango-page-contact-3"),
	url(r'^page-extended-portfolio/$', 'jango.views.navigation', {"template":"page-extended-portfolio.html"}, name="jango-page-extended-portfolio"),
	url(r'^page-faq-2/$', 'jango.views.navigation', {"template":"page-faq-2.html"}, name="jango-page-faq-2"),
	url(r'^page-faq/$', 'jango.views.navigation', {"template":"page-faq.html"}, name="jango-page-faq"),
	url(r'^page-fullwidth-gallery/$', 'jango.views.navigation', {"template":"page-fullwidth-gallery.html"}, name="jango-page-fullwidth-gallery"),
	url(r'^page-index-gallery/$', 'jango.views.navigation', {"template":"page-index-gallery.html"}, name="jango-page-index-gallery"),
	url(r'^page-lightbox-gallery/$', 'jango.views.navigation', {"template":"page-lightbox-gallery.html"}, name="jango-page-lightbox-gallery"),
	url(r'^page-masonry-gallery/$', 'jango.views.navigation', {"template":"page-masonry-gallery.html"}, name="jango-page-masonry-gallery"),
	url(r'^page-masonry-portfolio/$', 'jango.views.navigation', {"template":"page-masonry-portfolio.html"}, name="jango-page-masonry-portfolio"),
	url(r'^page-product-launch/$', 'jango.views.navigation', {"template":"page-product-launch.html"}, name="jango-page-product-launch"),
	url(r'^page-team/$', 'jango.views.navigation', {"template":"page-team.html"}, name="jango-page-team"),
	url(r'^shop-cart-empty/$', 'jango.views.navigation', {"template":"shop-cart-empty.html"}, name="jango-shop-cart-empty"),
	url(r'^shop-cart/$', 'jango.views.navigation', {"template":"shop-cart.html"}, name="jango-shop-cart"),
	url(r'^shop-checkout-complete/$', 'jango.views.navigation', {"template":"shop-checkout-complete.html"}, name="jango-shop-checkout-complete"),
	url(r'^shop-checkout/$', 'jango.views.navigation', {"template":"shop-checkout.html"}, name="jango-shop-checkout"),
	url(r'^shop-customer-account/$', 'jango.views.navigation', {"template":"shop-customer-account.html"}, name="jango-shop-customer-account"),
	url(r'^shop-customer-addresses/$', 'jango.views.navigation', {"template":"shop-customer-addresses.html"}, name="jango-shop-customer-addresses"),
	url(r'^shop-customer-dashboard/$', 'jango.views.navigation', {"template":"shop-customer-dashboard.html"}, name="jango-shop-customer-dashboard"),
	url(r'^shop-customer-profile/$', 'jango.views.navigation', {"template":"shop-customer-profile.html"}, name="jango-shop-customer-profile"),
	url(r'^shop-home-1/$', 'jango.views.navigation', {"template":"shop-home-1.html"}, name="jango-shop-home-1"),
	url(r'^shop-home-2/$', 'jango.views.navigation', {"template":"shop-home-2.html"}, name="jango-shop-home-2"),
	url(r'^shop-home-3/$', 'jango.views.navigation', {"template":"shop-home-3.html"}, name="jango-shop-home-3"),
	url(r'^shop-home-4/$', 'jango.views.navigation', {"template":"shop-home-4.html"}, name="jango-shop-home-4"),
	url(r'^shop-home-5/$', 'jango.views.navigation', {"template":"shop-home-5.html"}, name="jango-shop-home-5"),
	url(r'^shop-home-6/$', 'jango.views.navigation', {"template":"shop-home-6.html"}, name="jango-shop-home-6"),
	url(r'^shop-home-7/$', 'jango.views.navigation', {"template":"shop-home-7.html"}, name="jango-shop-home-7"),
	url(r'^shop-order-history-2/$', 'jango.views.navigation', {"template":"shop-order-history-2.html"}, name="jango-shop-order-history-2"),
	url(r'^shop-order-history/$', 'jango.views.navigation', {"template":"shop-order-history.html"}, name="jango-shop-order-history"),
	url(r'^shop-product-comparison/$', 'jango.views.navigation', {"template":"shop-product-comparison.html"}, name="jango-shop-product-comparison"),
	url(r'^shop-product-details-2/$', 'jango.views.navigation', {"template":"shop-product-details-2.html"}, name="jango-shop-product-details-2"),
	url(r'^shop-product-details-3/$', 'jango.views.navigation', {"template":"shop-product-details-3.html"}, name="jango-shop-product-details-3"),
	url(r'^shop-product-details-4/$', 'jango.views.navigation', {"template":"shop-product-details-4.html"}, name="jango-shop-product-details-4"),
	url(r'^shop-product-details/$', 'jango.views.navigation', {"template":"shop-product-details.html"}, name="jango-shop-product-details"),
	url(r'^shop-product-grid/$', 'jango.views.navigation', {"template":"shop-product-grid.html"}, name="jango-shop-product-grid"),
	url(r'^shop-product-list/$', 'jango.views.navigation', {"template":"shop-product-list.html"}, name="jango-shop-product-list"),
	url(r'^shop-product-search/$', 'jango.views.navigation', {"template":"shop-product-search.html"}, name="jango-shop-product-search"),
	url(r'^shop-product-wishlist/$', 'jango.views.navigation', {"template":"shop-product-wishlist.html"}, name="jango-shop-product-wishlist"),
	url(r'^sidebar-menu-1/$', 'jango.views.navigation', {"template":"sidebar-menu-1.html"}, name="jango-sidebar-menu-1"),
	url(r'^sidebar-menu-2/$', 'jango.views.navigation', {"template":"sidebar-menu-2.html"}, name="jango-sidebar-menu-2"),
	url(r'^sidebar-menu-fluid/$', 'jango.views.navigation', {"template":"sidebar-menu-fluid.html"}, name="jango-sidebar-menu-fluid"),
	url(r'^sidebar-menu-right/$', 'jango.views.navigation', {"template":"sidebar-menu-right.html"}, name="jango-sidebar-menu-right"),
	url(r'^sidebar-menu-static/$', 'jango.views.navigation', {"template":"sidebar-menu-static.html"}, name="jango-sidebar-menu-static"),
	url(r'^ajax/2col-portfolio/load-more/$', 'jango.views.navigation', {"template":"ajax-2col-portfolio-load-more.html"}, name="jango-ajax-2col-portfolio-load-more"),
	url(r'^ajax/4col-portfolio/load-more/$', 'jango.views.navigation', {"template":"ajax-4col-portfolio-load-more.html"}, name="jango-ajax-4col-portfolio-load-more"),
	url(r'^ajax/extended-portfolio/load-more/$', 'jango.views.navigation', {"template":"ajax-extended-portfolio-load-more.html"}, name="jango-ajax-extended-portfolio-load-more"),
	url(r'^ajax/fullwidth-gallery/load-more/$', 'jango.views.navigation', {"template":"ajax-fullwidth-gallery-load-more.html"}, name="jango-ajax-fullwidth-gallery-load-more"),
	url(r'^ajax/fullwidth-gallery/loadMore/$', 'jango.views.navigation', {"template":"ajax-fullwidth-gallery-loadMore.html"}, name="jango-ajax-fullwidth-gallery-loadMore"),
	url(r'^ajax/index-gallery/load-more/$', 'jango.views.navigation', {"template":"ajax-index-gallery-load-more.html"}, name="jango-ajax-index-gallery-load-more"),
	url(r'^ajax/lightbox-gallery/load-more/$', 'jango.views.navigation', {"template":"ajax-lightbox-gallery-load-more.html"}, name="jango-ajax-lightbox-gallery-load-more"),
	url(r'^ajax/lightbox-gallery/loadMore/$', 'jango.views.navigation', {"template":"ajax-lightbox-gallery-loadMore.html"}, name="jango-ajax-lightbox-gallery-loadMore"),
	url(r'^ajax/lightbox-gallery/project1/$', 'jango.views.navigation', {"template":"ajax-lightbox-gallery-project1.html"}, name="jango-ajax-lightbox-gallery-project1"),
	url(r'^ajax/lightbox-gallery/project10/$', 'jango.views.navigation', {"template":"ajax-lightbox-gallery-project10.html"}, name="jango-ajax-lightbox-gallery-project10"),
	url(r'^ajax/lightbox-gallery/project11/$', 'jango.views.navigation', {"template":"ajax-lightbox-gallery-project11.html"}, name="jango-ajax-lightbox-gallery-project11"),
	url(r'^ajax/lightbox-gallery/project12/$', 'jango.views.navigation', {"template":"ajax-lightbox-gallery-project12.html"}, name="jango-ajax-lightbox-gallery-project12"),
	url(r'^ajax/lightbox-gallery/project13/$', 'jango.views.navigation', {"template":"ajax-lightbox-gallery-project13.html"}, name="jango-ajax-lightbox-gallery-project13"),
	url(r'^ajax/lightbox-gallery/project2/$', 'jango.views.navigation', {"template":"ajax-lightbox-gallery-project2.html"}, name="jango-ajax-lightbox-gallery-project2"),
	url(r'^ajax/lightbox-gallery/project3/$', 'jango.views.navigation', {"template":"ajax-lightbox-gallery-project3.html"}, name="jango-ajax-lightbox-gallery-project3"),
	url(r'^ajax/lightbox-gallery/project4/$', 'jango.views.navigation', {"template":"ajax-lightbox-gallery-project4.html"}, name="jango-ajax-lightbox-gallery-project4"),
	url(r'^ajax/lightbox-gallery/project5/$', 'jango.views.navigation', {"template":"ajax-lightbox-gallery-project5.html"}, name="jango-ajax-lightbox-gallery-project5"),
	url(r'^ajax/lightbox-gallery/project6/$', 'jango.views.navigation', {"template":"ajax-lightbox-gallery-project6.html"}, name="jango-ajax-lightbox-gallery-project6"),
	url(r'^ajax/lightbox-gallery/project7/$', 'jango.views.navigation', {"template":"ajax-lightbox-gallery-project7.html"}, name="jango-ajax-lightbox-gallery-project7"),
	url(r'^ajax/lightbox-gallery/project8/$', 'jango.views.navigation', {"template":"ajax-lightbox-gallery-project8.html"}, name="jango-ajax-lightbox-gallery-project8"),
	url(r'^ajax/lightbox-gallery/project9/$', 'jango.views.navigation', {"template":"ajax-lightbox-gallery-project9.html"}, name="jango-ajax-lightbox-gallery-project9"),
	url(r'^ajax/masonry-gallery/load-more/$', 'jango.views.navigation', {"template":"ajax-masonry-gallery-load-more.html"}, name="jango-ajax-masonry-gallery-load-more"),
	url(r'^ajax/masonry-gallery/loadMore/$', 'jango.views.navigation', {"template":"ajax-masonry-gallery-loadMore.html"}, name="jango-ajax-masonry-gallery-loadMore"),
	url(r'^ajax/masonry-gallery/project1/$', 'jango.views.navigation', {"template":"ajax-masonry-gallery-project1.html"}, name="jango-ajax-masonry-gallery-project1"),
	url(r'^ajax/masonry-gallery/project10/$', 'jango.views.navigation', {"template":"ajax-masonry-gallery-project10.html"}, name="jango-ajax-masonry-gallery-project10"),
	url(r'^ajax/masonry-gallery/project11/$', 'jango.views.navigation', {"template":"ajax-masonry-gallery-project11.html"}, name="jango-ajax-masonry-gallery-project11"),
	url(r'^ajax/masonry-gallery/project12/$', 'jango.views.navigation', {"template":"ajax-masonry-gallery-project12.html"}, name="jango-ajax-masonry-gallery-project12"),
	url(r'^ajax/masonry-gallery/project13/$', 'jango.views.navigation', {"template":"ajax-masonry-gallery-project13.html"}, name="jango-ajax-masonry-gallery-project13"),
	url(r'^ajax/masonry-gallery/project14/$', 'jango.views.navigation', {"template":"ajax-masonry-gallery-project14.html"}, name="jango-ajax-masonry-gallery-project14"),
	url(r'^ajax/masonry-gallery/project15/$', 'jango.views.navigation', {"template":"ajax-masonry-gallery-project15.html"}, name="jango-ajax-masonry-gallery-project15"),
	url(r'^ajax/masonry-gallery/project16/$', 'jango.views.navigation', {"template":"ajax-masonry-gallery-project16.html"}, name="jango-ajax-masonry-gallery-project16"),
	url(r'^ajax/masonry-gallery/project17/$', 'jango.views.navigation', {"template":"ajax-masonry-gallery-project17.html"}, name="jango-ajax-masonry-gallery-project17"),
	url(r'^ajax/masonry-gallery/project18/$', 'jango.views.navigation', {"template":"ajax-masonry-gallery-project18.html"}, name="jango-ajax-masonry-gallery-project18"),
	url(r'^ajax/masonry-gallery/project2/$', 'jango.views.navigation', {"template":"ajax-masonry-gallery-project2.html"}, name="jango-ajax-masonry-gallery-project2"),
	url(r'^ajax/masonry-gallery/project3/$', 'jango.views.navigation', {"template":"ajax-masonry-gallery-project3.html"}, name="jango-ajax-masonry-gallery-project3"),
	url(r'^ajax/masonry-gallery/project4/$', 'jango.views.navigation', {"template":"ajax-masonry-gallery-project4.html"}, name="jango-ajax-masonry-gallery-project4"),
	url(r'^ajax/masonry-gallery/project5/$', 'jango.views.navigation', {"template":"ajax-masonry-gallery-project5.html"}, name="jango-ajax-masonry-gallery-project5"),
	url(r'^ajax/masonry-gallery/project6/$', 'jango.views.navigation', {"template":"ajax-masonry-gallery-project6.html"}, name="jango-ajax-masonry-gallery-project6"),
	url(r'^ajax/masonry-gallery/project7/$', 'jango.views.navigation', {"template":"ajax-masonry-gallery-project7.html"}, name="jango-ajax-masonry-gallery-project7"),
	url(r'^ajax/masonry-gallery/project8/$', 'jango.views.navigation', {"template":"ajax-masonry-gallery-project8.html"}, name="jango-ajax-masonry-gallery-project8"),
	url(r'^ajax/masonry-gallery/project9/$', 'jango.views.navigation', {"template":"ajax-masonry-gallery-project9.html"}, name="jango-ajax-masonry-gallery-project9"),
	url(r'^ajax/masonry-portfolio/load-more/$', 'jango.views.navigation', {"template":"ajax-masonry-portfolio-load-more.html"}, name="jango-ajax-masonry-portfolio-load-more"),
	url(r'^ajax/projects/project1/$', 'jango.views.navigation', {"template":"ajax-projects-project1.html"}, name="jango-ajax-projects-project1"),
	url(r'^ajax/projects/project10/$', 'jango.views.navigation', {"template":"ajax-projects-project10.html"}, name="jango-ajax-projects-project10"),
	url(r'^ajax/projects/project11/$', 'jango.views.navigation', {"template":"ajax-projects-project11.html"}, name="jango-ajax-projects-project11"),
	url(r'^ajax/projects/project12/$', 'jango.views.navigation', {"template":"ajax-projects-project12.html"}, name="jango-ajax-projects-project12"),
	url(r'^ajax/projects/project13/$', 'jango.views.navigation', {"template":"ajax-projects-project13.html"}, name="jango-ajax-projects-project13"),
	url(r'^ajax/projects/project14/$', 'jango.views.navigation', {"template":"ajax-projects-project14.html"}, name="jango-ajax-projects-project14"),
	url(r'^ajax/projects/project15/$', 'jango.views.navigation', {"template":"ajax-projects-project15.html"}, name="jango-ajax-projects-project15"),
	url(r'^ajax/projects/project16/$', 'jango.views.navigation', {"template":"ajax-projects-project16.html"}, name="jango-ajax-projects-project16"),
	url(r'^ajax/projects/project17/$', 'jango.views.navigation', {"template":"ajax-projects-project17.html"}, name="jango-ajax-projects-project17"),
	url(r'^ajax/projects/project18/$', 'jango.views.navigation', {"template":"ajax-projects-project18.html"}, name="jango-ajax-projects-project18"),
	url(r'^ajax/projects/project2/$', 'jango.views.navigation', {"template":"ajax-projects-project2.html"}, name="jango-ajax-projects-project2"),
	url(r'^ajax/projects/project3/$', 'jango.views.navigation', {"template":"ajax-projects-project3.html"}, name="jango-ajax-projects-project3"),
	url(r'^ajax/projects/project4/$', 'jango.views.navigation', {"template":"ajax-projects-project4.html"}, name="jango-ajax-projects-project4"),
	url(r'^ajax/projects/project5/$', 'jango.views.navigation', {"template":"ajax-projects-project5.html"}, name="jango-ajax-projects-project5"),
	url(r'^ajax/projects/project6/$', 'jango.views.navigation', {"template":"ajax-projects-project6.html"}, name="jango-ajax-projects-project6"),
	url(r'^ajax/projects/project7/$', 'jango.views.navigation', {"template":"ajax-projects-project7.html"}, name="jango-ajax-projects-project7"),
	url(r'^ajax/projects/project8/$', 'jango.views.navigation', {"template":"ajax-projects-project8.html"}, name="jango-ajax-projects-project8"),
	url(r'^ajax/projects/project9/$', 'jango.views.navigation', {"template":"ajax-projects-project9.html"}, name="jango-ajax-projects-project9"),
)	

