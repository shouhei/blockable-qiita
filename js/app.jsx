'use strict'
//var React = require('react');
//var request = require('superagent');
import React from 'react';
import request from 'superagent';
import RaisedButton from 'material-ui/lib/raised-button';
import AppBar from 'material-ui/lib/app-bar';
import List from 'material-ui/lib/lists/list';
import ListItem from 'material-ui/lib/lists/list-item';


var App = React.createClass({
  getInitialState: function(){
     return {
         items: [],
     }
  },
    onAdd: function(newItem){
      this.state.items.push(newItem);
      this.setState({
        items : this.state.items
      });
  },
  render: function(){
    return (
      <div className="container">
        <AppBar
           title="Blockable-Qiita"
        />
        <Items items={this.state.items}/>
        <More onAdd={this.onAdd}/>
      </div>
    );
  }
});

var Items = React.createClass({
    render: function(){
    return(
      <List>
      {
        this.props.items.map(function(item, i){
            //return <li><a href={item['url']}>{item['title']}</a></li>
            return <ListItem primaryText={<a href={item['url']} target='_blank'>{item['title']}</a>} />
          })
      }
      </List>
    )
  }
});

var More = React.createClass({
    getInitialState: function(){
        return {page: 1}
    },
    clickHandler: function(){
        this.setState({page: this.state.page+1});
        var that = this;
        var data = request
            .get("/feeds/" + this.state.page)
            .end(function(err, res){
                for(var i = 0; i < res.body.length; i++){
                  that.props.onAdd({'title': res.body[i]['title'], 'url': res.body[i]['url']});
                }
            });
    },
    render: function(){
        return (<RaisedButton onClick={this.clickHandler} label="more" />)
    }
});

React.render(
  <App />,
  document.querySelector('body')
);
