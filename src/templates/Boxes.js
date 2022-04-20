import React from 'react';
import { StyleSheet, Text, View } from 'react-native';
import { Button, TouchableWithoutFeedback} from 'react-native-web';

const Boxes = ({ navigation }) => {
    return(
      <View style={styles.container}>
        <View style={styles.box}>
          <View style={styles.inner}>
          <Button title='Left' onPress={() => navigation.navigate('Robot', {direction: 'left'})}/>
          </View>
        </View>
        <View style={styles.box}>
          <View style={styles.inner}>
          <Button title='Right' onPress={() => navigation.navigate('Robot', {direction: 'right'})}/>
          </View>
        </View>
        <View style={styles.box}>
          <View style={styles.inner}>
          <Button title='Scan' onPress={() => navigation.navigate('Camera')}/>
          </View>
        </View>
        <View style={styles.box}>
          <View style={styles.inner}>
          <Button title='Start'/>
          </View>
        </View>
      </View>
    )
  }

  export default Boxes;

const styles = StyleSheet.create({
  container: {
    width: '100%',
    height: '85%',
    padding: 5,
    flexDirection: 'row',
    flexWrap: 'wrap'
  },
  box: {
    width: '50%',
    height: '50%',
    padding: 5
  },
  inner: {
    flex: 1,
    backgroundColor: '#eee',
    alignItems: 'center',
    justifyContent: 'center'
  }
})