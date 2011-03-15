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
		this.addEvents(
			/**
			* @event addusers Event declaration
			*/
			'addusers',
			/**
			* @event removeusers Event declaration
			*/
			'removeusers'
		);
		
		Phi.model.Workspace.superclass.initComponent.call(config);
	}
	,
	/**
	* add user into workspace user collection
	* @param {integer} id workspace id (key)
	* @param {Array} userName array with user name (key)
	* */
	addUsers: function (id, userNames) {
		var params = {
			id: id,
			userNames: userNames
		}

		Ext.Ajax.request({
			url: Phi.UriTemplate.getUri('workspaceAddUsers'),
			method: 'POST',
			headers: { 'Content-Type': 'text/json' },
			jsonData: params,
			scope: this,
			success: function (response, options) {
				var o = Ext.util.JSON.decode(response.responseText);
				this.fireEvent('addusers', o);
			}
		});
	}
	,
	/**
	* remove user into workspace user collection
	* @param {integer} id workspace id (key)
	* @param {Array} userName array with user name (key)
	* */
	removeUsers: function (id, userNames) {
		var params = {
			id: id,
			userNames: userNames
		}

		Ext.Ajax.request({
			url: Phi.UriTemplate.getUri('workspaceRemoveUsers'),
			method: 'POST',
			headers: { 'Content-Type': 'text/json' },
			jsonData: params,
			scope: this,
			success: function (response, options) {
				var o = Ext.util.JSON.decode(response.responseText);
				this.fireEvent('removeusers', o);
			}
		});
	}
});