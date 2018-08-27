var app = new Vue({
    el: '#cardSet',
		delimiters: ['${','}'],
		http: {
        root: 'http://localhost:8000/',
        headers: {
					// Authorization: 'Token c39a04212685d3d4780ed90fab0b6914579f4af7',
					// csrftoken: Cookies.get('csrftoken'),
        },
		},
    data: {
        heading: 'Set Name or Student?',
				target_set: 0, //the user will enter this. currently the text data only has 1 set
				cards: [], // this should populate with a list of dictionaries containing all the info to build the cards. OJO! there may be multiple images at some
				test: [
					{'text':'hello?'},
					{'text':'is anyone there?'}],
				sets: [],


    },
    methods: {
			getCards: function() {
				console.log('you called getCards')
					this.$http.get('sets/')
							.then((response) => {
									// console.log(response.body)
									this.sets = response.body;
									for (let i=0; i<this.sets.length; i++) {
										for (let j=0; j<this.sets[i].cards.length; j++){
										// this.cards.push(this.sets[i]['cards']['text'])
										// console.log(this.sets[i]['cards']['text'])
										console.log(this.sets[i].cards[j].text)
										}
										// set = this.sets[i]
										// console.log(this.cards)
									}
								  console.log(this.sets)
							})
							.catch((err) => {
									console.log(err);
							});
			},
			sayHi: function() {
				console.log("hello!")
			},
		},
		mounted: function() {
			this.sayHi();
			this.getCards();
		},
});
