// Generated by gencpp from file segmentation/wound.msg
// DO NOT EDIT!


#ifndef SEGMENTATION_MESSAGE_WOUND_H
#define SEGMENTATION_MESSAGE_WOUND_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace segmentation
{
template <class ContainerAllocator>
struct wound_
{
  typedef wound_<ContainerAllocator> Type;

  wound_()
    : x(0.0)
    , y(0.0)
    , length(0.0)
    , width(0.0)  {
    }
  wound_(const ContainerAllocator& _alloc)
    : x(0.0)
    , y(0.0)
    , length(0.0)
    , width(0.0)  {
  (void)_alloc;
    }



   typedef double _x_type;
  _x_type x;

   typedef double _y_type;
  _y_type y;

   typedef double _length_type;
  _length_type length;

   typedef double _width_type;
  _width_type width;





  typedef boost::shared_ptr< ::segmentation::wound_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::segmentation::wound_<ContainerAllocator> const> ConstPtr;

}; // struct wound_

typedef ::segmentation::wound_<std::allocator<void> > wound;

typedef boost::shared_ptr< ::segmentation::wound > woundPtr;
typedef boost::shared_ptr< ::segmentation::wound const> woundConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::segmentation::wound_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::segmentation::wound_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace segmentation

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': True, 'IsMessage': True, 'HasHeader': False}
// {'segmentation': ['/home/cc/ee106a/fa19/class/ee106a-aft/ros_workspaces/lab7/src/segmentation/msg'], 'std_msgs': ['/opt/ros/kinetic/share/std_msgs/cmake/../msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::segmentation::wound_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::segmentation::wound_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::segmentation::wound_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::segmentation::wound_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::segmentation::wound_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::segmentation::wound_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::segmentation::wound_<ContainerAllocator> >
{
  static const char* value()
  {
    return "e1d56a1459316f615661d9730e39e6a7";
  }

  static const char* value(const ::segmentation::wound_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xe1d56a1459316f61ULL;
  static const uint64_t static_value2 = 0x5661d9730e39e6a7ULL;
};

template<class ContainerAllocator>
struct DataType< ::segmentation::wound_<ContainerAllocator> >
{
  static const char* value()
  {
    return "segmentation/wound";
  }

  static const char* value(const ::segmentation::wound_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::segmentation::wound_<ContainerAllocator> >
{
  static const char* value()
  {
    return "float64 x\n\
float64 y\n\
float64 length\n\
float64 width\n\
";
  }

  static const char* value(const ::segmentation::wound_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::segmentation::wound_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.x);
      stream.next(m.y);
      stream.next(m.length);
      stream.next(m.width);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct wound_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::segmentation::wound_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::segmentation::wound_<ContainerAllocator>& v)
  {
    s << indent << "x: ";
    Printer<double>::stream(s, indent + "  ", v.x);
    s << indent << "y: ";
    Printer<double>::stream(s, indent + "  ", v.y);
    s << indent << "length: ";
    Printer<double>::stream(s, indent + "  ", v.length);
    s << indent << "width: ";
    Printer<double>::stream(s, indent + "  ", v.width);
  }
};

} // namespace message_operations
} // namespace ros

#endif // SEGMENTATION_MESSAGE_WOUND_H
