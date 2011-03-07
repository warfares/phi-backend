Ext.ns("Phi.model");
/**
 * @class Phi.model.Workspace 
 * @extends Phi.model.Entity
 * 
 * Philosophy Workspace Proxy
 * 
 * @author rbarriga
 * @version 1.0
 * @copyright (c) 2011, by rbarriga
 * @date      15. February 2011
 *
 */
Phi.model.Workspace = Ext.extend(Phi.model.Entity, {
	entityURL: Phi.UriTemplate.getUri('workspace'),

	initComponent: function (config) {
		Phi.model.Workspace.superclass.initComponent.call(config);
	}
});