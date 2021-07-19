import { Base } from "./base.js"

export class Scatter extends Base {
	constructor( _target, _data ) {
		super( _target, _data );

		this.hours_bins = null;
		this.experience_bins = null;

		this.init();
	}

	init() {
		// Define this vis
		const vis = this;

		super.init();

		this.tooltip = this.parent.append( 'div' )
			.attr( 'id', this.id + "_tooltip" )
			.attr( 'class', 'tooltip' )
			.style( "opacity", 0 )
			.append( 'p' )

		// center the graph
		vis.g.style('transform', `translate(${vis.gMargin.left}px, ${vis.gMargin.top - 15}px)`)

		// set the scale
		this.axes.x.scale = [ 0, d3.max( this.data, d => d.experience_yr ) ];
		this.axes.x.link = d3.scaleLinear()
			.domain( this.axes.x.scale )
			.range( [ 0, this.gW ] );

		this.axes.y.scale = [ 0, d3.max( this.data, d => d.hw1_hrs ) ];
		this.axes.y.link = d3.scaleLinear()
			.domain( this.axes.y.scale )
			.range( [ this.gH, 0 ] );
		
		vis.histogram = d3.histogram();

		vis.wrangle();
	}

	wrangle() {
		const vis = this;

		// lets figure out how variable the hours are
		vis.hours_bins = d3.rollups( vis.data, v => v.length, d => d.hw1_hrs )

		// lets figure out how variable the experiences are
		vis.experience_bins = d3.rollups( vis.data, v => v.length, d => d.experience_yr )

		this.render();
	}
	
	// v4,5 method
	// wrangle() {
	// 	// let's use d3.nest() to figure out how many different ages there are
	// 	this.hours_bins = d3.nest()
	// 		.key( d => d.hw1_hrs )                   // looking at ages
	// 		.rollup( d => d3.sum( d, g => 1 ) )  // we want to count each one
	// 		.entries( vis.data )                    // taking entries from the data
	// 		
	// 	// v4,5 method
	// 	this.experience_bins = d3.nest()
	// 		.key( d => d.experience_yr )         // looking at experience
	// 		.rollup( d => d3.sum( d, g => 1 ) )  // we want to count each one
	// 		.entries( vis.data )                    // taking entries from the data
	// }

	render() {
		const vis = this;

		let step = {
			x : vis.gW / vis.experience_bins.length,
			y : vis.gH / vis.hours_bins.length
		};

		// Draw the axes
		let x_axis = this.g.append( 'g' )
			.attr( 'transform', `translate(${(vis.gMargin.left - step.x) }, ${ vis.gH + step.y })`)
			.attr("foo", "bar")
			.call( d3.axisBottom( vis.axes.x.link ) );
		
		x_axis.append( 'text' )
			.text( "Years of Experience" )
			.attr( 'class', 'label' )
			.attr( 'text-anchor', 'middle' )
			.attr( 'x', vis.gW / 2 )
			.attr( 'dy', '2.5em' )

		let y_axis = this.g.append( 'g' )
			.attr( 'transform', `translate(${vis.gMargin.left - ( step.x * 2 ) }, 0)`)
			.call( d3.axisLeft( vis.axes.y.link ) );
		
		y_axis.append( 'text' )
			.text( 'Homework Hours' )
			.attr( 'class', 'label' )
			.attr( 'text-anchor', 'middle' )
			.attr( 'transform', 'rotate(-90)' )
			.attr( 'x', -( vis.gH / 2 ) )
			.attr( 'y', -vis.gMargin.left  )
			.attr( 'dy', "1em" )


		// draw the data
		let dots = this.g.append( 'g' )
			.attr( 'transform', `translate(${vis.gMargin.left - step.x }, ${vis.gH / vis.hours_bins.length - step.y })`)
			.selectAll( "circle" )
			.data( vis.data )
			.enter()
			.append( "circle" )
			.attr( 'id', ( d, i ) => this.id + "_dot_" + i )
			.attr( "cx", d => vis.axes.x.link( d.experience_yr ) )
			.attr( "cy", d => vis.axes.y.link( d.hw1_hrs ) )
			.attr( 'r0', d => d.age / vis.axes.x.scale[ 1 ] )
			.style( 'fill', "#69b3a2" )
			.attr( 'f0', "#69b3a2" )
			// HW: HANDLE mouseover and mouseout
			// HW: Transition to show the dots over time
				.attr( "r", d => d.age / vis.axes.x.scale[ 1 ] ) // normalize the age between [0,max] => [0,1]

	}


	handleMouseOver( e, d, i ) {
		// HW: Show a tooltip positioned next to the dot, containing the user's name and age (can you fade it in?)
		// HW: Transition the color from the one displayed to some other color of your choice
		// HW: Transition the radius to a diameter of 10
	}

	handleMouseOut( e, d, i ) {
		// HW: Hide/remove the tooltip (can you fade it out?)
		// HW: Transition back to the original color
		// HW: Transition the radius back to its original size
	}
}
export default Scatter;
