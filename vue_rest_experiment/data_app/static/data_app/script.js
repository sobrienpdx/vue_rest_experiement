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
				// cards: [], // this should populate with a list of dictionaries containing all the info to build the cards. OJO! there may be multiple images at some
				test: [
					{'text':'hello?'},
					{'text':'is anyone there?'}],
				sets: [],
				card_number: 0,
				score: 100,
				correcty: 0,
				incorrecty: 0,


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

			next: function() {
				this.card_number += 1
				console.log(this.card_number)
			},
			printNewScore: function() {
				console.log('you called update score')
				this.score = Math.round((this.correcty/(this.correcty + this.incorrecty))*100)

				console.log(this.correcty)
				// this.$http.get('scores/', 'score')
				// 	.then((response) => {
				// 			this.score=score
				// 	})
				// 	.catch((err) => {
				// 			console.log(err);
				// 	});
			},


			scoreCorrect: function(id) {
				console.log("you called correct")
				this.correcty +=1
				this.$http.patch(`scores/${id}/`, {'correct': this.correcty})
						.then((response) => {
								console.log(response.body)
								let scorey = response.body
								console.log(scorey.correct)
						})
						this.printNewScore()
			},

			scoreIncorrect: function(id) {
				console.log("you called incorrect")
				this.incorrecty +=1
				this.$http.patch(`scores/${id}/`, {'incorrect': this.incorrecty})
						.then((response) => {
								console.log(response.body)
								let scorey = response.body
								console.log(scorey.incorrect)
						})
						this.printNewScore()
			},


			sayHi: function() {
				console.log("hello!")
			},




		},
		mounted: function() {
			// this.sayHi();
			this.getCards();
		},
});
