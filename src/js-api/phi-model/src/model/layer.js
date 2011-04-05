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
	,
	/**
	* Read entity (override)... 
	* NOTE: override cause  WCF compatibility problems (special characters..in this case dot)
	* @param {String} entity identification (key)
	*/
	read: function (layerName) {
		var p = {
			layerName:layerName
		};
		
		Ext.Ajax.request({
			url: this.entityURL + '?' + Ext.urlEncode(p),
			scope:this,
			success: function (r, opt) {
				var o = Ext.util.JSON.decode(r.responseText);
				this.fireEvent('read', o);
			}
		});
	}
});