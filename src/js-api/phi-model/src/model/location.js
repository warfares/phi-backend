Ext.ns("Phi.model");
/**
 * @class Phi.model.Location 
 * @extends Phi.model.Entity
 * 
 * Philosophy Location Proxy
 * 
 * @author rbarriga
 * @version 1.0
 * @copyright (c) 2011, by rbarriga
 * @date      15. February 2011
 *
 */
Phi.model.Location = Ext.extend(Phi.model.Entity, {
	entityURL: Phi.UriTemplate.getUri('location'),
	
	initComponent: function (config) {
		this.addEvents(
			/**
			* @event favorite Event declaration
			*/
			'favorite'
		);
		
		Phi.model.Location.superclass.initComponent.call(config);
	}
	,
	favorite: function (id, favorite) {
		
		var o = {
			id: id,
			favorite: favorite
		}

		Ext.Ajax.request({
			url: Phi.UriTemplate.getUri('locationFavorite'),
			method: 'POST',
			headers: { 'Content-Type': 'text/json' },
			jsonData: o,
			scope: this,
			success: function (response, options) {
				var response = Ext.util.JSON.decode(response.responseText);
				this.fireEvent('favorite', response);
			}
		});
	}
});