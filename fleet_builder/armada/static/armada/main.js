let app = new Vue({
    el: "#app",
    delimiters: ['xxx', 'xxx'],
    data: {
        message: 'hello',
        // [] = lists, {} = dictionaries
        // base variables are lists of all available. 
        // specific ships/squads/objects are dictonaries
        baseShips: [],
        SelectedShip: {},
        baseSquadrons: [],
        squadrons: {},
        baseObjectives: [],
        objectives: {},
        shipUpgrades: [],
        upgradeTypes: [],
        displayUpgradeType: [],
        token: ''
    },

    methods: {
        getBaseShips: async function (faction) {
            data = await axios.get(`getBaseShips/${faction}/`)
            app.baseShips = data.data.base_ships

        },

        selectShip: async function (ship_id) {
            data = await axios.get(`getSingleShip/${ship_id}/`)
            app.SelectedShip = data.data.ship
            app.baseShips = []
            app.SelectedShip.upgrades = []
            app.shipUpgrades = data.data.upgrades
            for (upgrade of app.shipUpgrades) {
                let found = app.upgradeTypes.some(el => upgrade.upgrade_icon.upgrade_type === el.upgrade_type)
                if (!found){
                    app.upgradeTypes.push(upgrade.upgrade_icon)
                }
            }
        },

        displayAllUpgradeType: function (upgrade_type) {
            app.displayUpgradeType = []
            for (upgrade of app.shipUpgrades) {  
                if (upgrade.upgrade_type == upgrade_type.replace('_', ' ') && (upgrade.ship == '' || upgrade.ship == app.SelectedShip.ship_type)) {
                    app.displayUpgradeType.push(upgrade)         
                }
            }
        },

        addAvailableUpgrade: function (upgrade) {
            for ([i, {upgrade_type}] of app.SelectedShip.upgrades.entries()){
                if (upgrade_type == upgrade.upgrade_type){       
                    app.SelectedShip.upgrades.splice(i,1)
                }
            }

            app.SelectedShip.upgrades.push(upgrade)
            app.displayUpgradeType = []
            for (button of app.upgradeTypes){
                if (button.upgrade_type.replace('_', ' ') == upgrade.upgrade_type){
                    button.path = upgrade.image
                }  
            }
        },

        saveShip: async function() {
            let token = document.getElementsByName('csrfmiddlewaretoken')[0]
            data = await axios.post(`saveShip/`, {
                headers: {
                    'X-CSRFToken': token.value
                },
                data: {
                    ship: app.SelectedShip
                }
            })
            location.reload()
        },
        allUserShips: async function() {
            let token = document.getElementsByName('csrfmiddlewaretoken')[0]
            data = await axios.get()




        }
    },

    created: function () {
            

    }
})