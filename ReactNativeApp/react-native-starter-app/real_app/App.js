import React, { Component } from 'react';
import { StyleSheet, Text, View, TouchableHighlight } from 'react-native';
// import ViewRecipe  from './screens/ViewRecipe';


var steps = [{"stepNumber": 1, "text": "Preheat oven to 350 degrees F (175 degrees C).\n", "lengthMins": "", "lengthHours": "", "lengthSecs": 3},
{"stepNumber": 2, "text": "Cream together the butter, white sugar, and brown sugar until smooth.\n", "lengthMins": "", "lengthHours": "", "lengthSecs": 4},
{"stepNumber": 3, "text": "Beat in the eggs one at a time, then stir in the vanilla.\n", "lengthMins": "", "lengthHours": "", "lengthSecs": 5},
{"stepNumber": 4, "text": "Dissolve baking soda in hot water.\n", "lengthMins": 1, "lengthHours": "", "lengthSecs": ""},
{"stepNumber": 5, "text": "Add to batter along with salt.\n", "lengthMins": 1, "lengthHours": "", "lengthSecs": ""},
{"stepNumber": 6, "text": "Stir in flour, chocolate chips, and nuts.\n", "lengthMins": "", "lengthHours": "", "lengthSecs": 3},
{"stepNumber": 7, "text": "Drop by large spoonfuls onto ungreased pans.\n", "lengthMins": "", "lengthHours": "", "lengthSecs": 12},
{"stepNumber": 8, "text": "Bake for about 10 minutes in the preheated oven, or until edges are nicely browned.\n", "lengthMins": 10, "lengthHours": "", "lengthSecs": ""},
];

class CountdownTimer extends Component {
  constructor(props) {
    super(props);
  }

  render() {
    if (!this.props.secondsLeft) return null;
    return (
      <View>
        <Text>{ this.props.secondsLeft }</Text>
      </View>
    );
  }

}

class ViewRecipe extends Component {
  constructor(props){
    super(props);
    this.state = {
      recipeTitle : "Hard boiled eggs",
      currentStep : 0,
      secondsLeft : 0
    }
    this.getCurrStepTimeSecs = this.getCurrStepTimeSecs.bind(this);
    this.startCurrStep = this.startCurrStep.bind(this);
  }

  getCurrStepTimeSecs() {
    var currStep = this.props.steps[this.state.currentStep];
    var result = currStep.lengthHours * 3600 || currStep.lengthMins * 60 || currStep.lengthSecs;
    return result;
  }

  getSteps() {
    var steps =  this.props.steps.map((step, i) => (
    <Text key={'step'+i}
      style={ i == this.state.currentStep ? styles.activeStep : styles.inactiveStep }>
      {step.text}
      </Text>));

    return <View>
      {steps}
      </View>
  }

  startTimer() {
    var stepLength = this.getCurrStepTimeSecs();
    if (!stepLength) {
      return;
    };
    this.setState( { secondsLeft : stepLength });
    var interval = setInterval(()=>{
      if (this.state.secondsLeft > 0) {
        this.setState({ secondsLeft : this.state.secondsLeft - 1 });
      };
    }, 1000);
    setTimeout(()=>{
      clearInterval(interval);
    }, stepLength * 1000);
  }

  startCurrStep() {
    var stepLengthSecs = this.getCurrStepTimeSecs();
    if (stepLengthSecs) {
      this.startTimer();
      setTimeout(()=>{
        this.setState({
          currentStep : this.state.currentStep + 1
        });
        if (this.state.currentStep < this.props.steps.length - 1) {
          this.startCurrStep();
        }
      }, stepLengthSecs * 1000);

      // var currStepCountdown = setInterval(()=>{

      // });

    } else {

    }
  }

  render() {
    return (
      <View>
          <TouchableHighlight onPress={this.startCurrStep}>
            <Text>Cook</Text>
            </TouchableHighlight>

            <CountdownTimer secondsLeft={this.state.secondsLeft}/>
          <Text>
              { this.state.recipeTitle }
          </Text>
          { this.getSteps() }
      </View>
    );
  }
}

export default class App extends React.Component {
  render() {
    return (
      <View style={styles.container}>
        <ViewRecipe steps={steps}/>
      </View>
    );
  }
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    // backgroundColor: '#fff',
    backgroundColor : 'aquamarine',
    alignItems: 'center',
    justifyContent: 'center',
  },
  activeStep : {
    fontSize : 25,
    color: 'red'
  },
  inactiveStep : {

  }
});
