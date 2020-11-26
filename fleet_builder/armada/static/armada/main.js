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
    },

    methods: {
        getBaseShips: async function (faction) {
            data = await axios.get(`getBaseShips/${faction}/`)
            app.baseShips = data.data.base_ships

        },

        selectShip: async function (ship_id) {
            console.log(ship_id)
            data = await axios.get(`getSingleShip/${ship_id}/`)
            app.SelectedShip = data.data.ship
            app.baseShips = []
            app.SelectedShip.upgrades = []
            app.shipUpgrades = data.data.upgrades
            // for (upgrades of app.shipUpgrades){
            //     if (!app.upgradeTypes.includes(upgrades)){
            //         app.upgradeTypes.push(upgrades)
            //     }
            // }
            for (upgrade of app.shipUpgrades) {
                let found = app.upgradeTypes.some(el => upgrade.upgrade_icon === el)
                if (!found){
                    app.upgradeTypes.push(upgrade.upgrade_icon)
                }
            }
        },

        displayAllUpgradeType: function (upgrade_type) {
            app.displayUpgradeType = []
            for (upgrade of app.shipUpgrades) {
                if (upgrade.upgrade_type == upgrade_type && (upgrade.ship == '' || upgrade.ship == app.SelectedShip.ship_type)) {
                    app.displayUpgradeType.push(upgrade)
                }

            }

        },

        addAvailableUpgrade: function (upgrade) {

            app.SelectedShip.upgrades.push(upgrade)
            app.displayUpgradeType = []



        },

        removeAvailableUpgrade: function (upgrade) {

        },

    },

    created: function () {

    }
})