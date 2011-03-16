Ext.ns("Phi.model");
/**
 * @class Phi.model.Role 
 * @extends Phi.model.Entity
 * 
 * Philosophy Role Proxy
 * 
 * @author rbarriga
 * @version 1.0
 * @copyright (c) 2011, by rbarriga
 *
 */
Phi.model.Role = Ext.extend(Phi.model.Entity, {
	entityURL: Phi.UriTemplate.getUri('role'),

	initComponent: function (config) {
		this.addEvents(
			/**
			* @event getroles Event declaration
			*/
			'getroles'
		);
		
		Phi.model.Role.superclass.initComponent.call(config);
	}
	,
	/**
	*  Retrieve all roles.
	*
	* */
	getRoles: function () {
		Ext.Ajax.request({
			url: Phi.UriTemplate.getUri('roles'),
			method: 'GET',
			headers: { 'Content-Type': 'text/json' },
			scope: this,
			success: function (response, options) {
				var o = Ext.util.JSON.decode(response.responseText);
				this.fireEvent('getroles', o);
			}
		});
	}
});