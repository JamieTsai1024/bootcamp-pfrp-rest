import React from 'react';

import './AddRestaurant.scss';

/**
 * This is a stateful function component using React Hooks
 */
const AddRestaurant = ({ loadData, storeData }) => {
  /**
   * if you've used class components before, the useState hook is similar to this code block:
   *
   * constructor(props) {
   *   super(props);
   *   this.state = {
   *     data: []
   *   };
   * }
   *
   * setData is a function used to update data, similar to this.setState({ data: ["my", "new", "data"] })
   */

  /**
   * useEffect is a hook used to apply side effects to the component, it can be used for fetching data.
   * similar to componentDidMount and componentDidUpdate, it runs when the component mounts or updates
   *
   * the second argument ([loadData] in this case) is an array of variables that the hook depends on,
   * the hook is only activated if one of those variables change
   */

  return (
    <div className='display-container'>
      <form>
        <label for='fname'>Restaurant name:</label>
        <input type='text' id='fname' name='fname' value='Campus Pizza' />
        <br />
        <label for='lname'>Address:</label>
        <input type='text' id='lname' name='lname' value='10 University Ave.' />
        <br />
        <input type='submit' value='Submit' />
      </form>
    </div>
  );
};

export default AddRestaurant;

AddRestaurant.propTypes = {};
