Ext.ns("Phi.model");
/**
 * @class Phi.model.Layer 
 * @extends Phi.model.Entity
 * 
 * Philosophy Layer Proxy
 * 
 * @author rbarriga
 * @version 1.0
 * @copyright (c) 2011, by rbarriga
 * @date      15. February 2011
 *
 */
Phi.model.Layer = Ext.extend(Phi.model.Entity, {
	entityURL: Phi.UriTemplate.getUri('layer'),

	initComponent: function (config) {
		Phi.model.Layer.superclass.initComponent.call(config);
	}
});