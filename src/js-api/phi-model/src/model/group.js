Ext.ns("Phi.model");
/**
 * @class Phi.model.Group 
 * @extends Phi.model.Entity
 * 
 * Philosophy Group Proxy
 * 
 * @author rbarriga
 * @version 1.0
 * @copyright (c) 2011, by rbarriga
 *
 */
Phi.model.Group = Ext.extend(Phi.model.Entity, {
	entityURL: Phi.UriTemplate.getUri('group'),

	initComponent: function (config) {
		this.addEvents(
			/**
			* @event getroles Event declaration
			*/
			'getgroups'
		);
		Phi.model.Group.superclass.initComponent.call(config);
	}
	,
	/**
	*  Retrieve all groups.
	*
	* */
	getGroups: function () {
		Ext.Ajax.request({
			url: Phi.UriTemplate.getUri('groups'),
			method: 'GET',
			headers: { 'Content-Type': 'text/json' },
			scope: this,
			success: function (response, options) {
				var o = Ext.util.JSON.decode(response.responseText);
				this.fireEvent('getgroups', o);
			}
		});
	}
});