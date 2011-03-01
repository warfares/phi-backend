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
		Phi.model.Location.superclass.initComponent.call(config);
	}
});