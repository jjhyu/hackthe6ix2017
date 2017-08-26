import React, { Component } from 'react';
import { StyleSheet, Text, View } from 'react-native';
// import ViewRecipe  from './screens/ViewRecipe';


var steps = [{"stepNumber": 1, "text": "Preheat oven to 350 degrees F (175 degrees C).\n", "lengthMins": "", "lengthHours": "", "lengthSecs": ""},
{"stepNumber": 2, "text": "Cream together the butter, white sugar, and brown sugar until smooth.\n", "lengthMins": "", "lengthHours": "", "lengthSecs": ""},
{"stepNumber": 3, "text": "Beat in the eggs one at a time, then stir in the vanilla.\n", "lengthMins": "", "lengthHours": "", "lengthSecs": ""},
{"stepNumber": 4, "text": "Dissolve baking soda in hot water.\n", "lengthMins": "", "lengthHours": "", "lengthSecs": ""},
{"stepNumber": 5, "text": "Add to batter along with salt.\n", "lengthMins": "", "lengthHours": "", "lengthSecs": ""},
{"stepNumber": 6, "text": "Stir in flour, chocolate chips, and nuts.\n", "lengthMins": "", "lengthHours": "", "lengthSecs": ""},
{"stepNumber": 7, "text": "Drop by large spoonfuls onto ungreased pans.\n", "lengthMins": "", "lengthHours": "", "lengthSecs": ""},
{"stepNumber": 8, "text": "Bake for about 10 minutes in the preheated oven, or until edges are nicely browned.\n", "lengthMins": 10, "lengthHours": "", "lengthSecs": ""},
];

class ViewRecipe extends Component {
  constructor(props){
    super(props);
    this.state = {
      recipeTitle : "Hard boiled eggs",
      currentStep : 0
    }
  }

  getSteps() {
    var steps =  this.props.steps.map((step, i) => (
    <Text key={'step'+i}>
      {step.text}
      </Text>));
    
    
    return <View>
      {steps}
      </View>
  }

  render() {
    return (
      <View>
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
    backgroundColor : 'red',
    alignItems: 'center',
    justifyContent: 'center',
  },
});
